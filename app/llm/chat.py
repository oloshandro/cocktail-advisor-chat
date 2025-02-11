from app.llm.utils import read_csv_file
from app.llm.prompt_helpers import create_rag_chain
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_core.runnables.history import RunnableWithMessageHistory


class RagGenerator:
    def __init__(self, data_path, vectorstore_path):
        self.data_path = data_path 
        self.vectorstore_path = vectorstore_path
        self.embeddings = None
        self.vectordb = None
        self.retriever = None
       
    def initialize(self):
        self.initialize_embedding_model()
        self.create_vector_db()
        self.initialize_retriever()
    
    
    def initialize_embedding_model(self):
        self.embeddings = OpenAIEmbeddings()

    @staticmethod
    def get_documents_from_csv(df):
        """convert CSV text column into Document objects"""
        text_chunks = df["text"].dropna().tolist()
        documents = [Document(page_content=chunk) for chunk in text_chunks]
        return documents
            
    def create_vector_db(self):
        """generate_data_store """
        df = read_csv_file(self.data_path)
        documents = self.get_documents_from_csv(df)

        vectordb = FAISS.from_documents(
            documents=documents, 
            embedding=self.embeddings
            )
        self.vectordb = vectordb.save_local(self.vectorstore_path)
        print(f"Saved {len(documents)} chunks to {self.vectorstore_path}.")
        print("Completed generation of datastore")
        
    def initialize_retriever(self):
        try:
            self.retriever = FAISS.load_local(
                self.vectorstore_path,
                self.embeddings,
                allow_dangerous_deserialization=True
                ).as_retriever(search_type='similarity', search_kwargs={"k": 3})
        except Exception as e:
            print(f"Error initializing retriever: {e}")
            
        return self.retriever


class CocktailChat(RagGenerator):
    def __init__(self, data_path, chroma_path, model, temperature):
        super().__init__(data_path, chroma_path)

        self.model = model
        self.temperature = temperature
        self.llm = self.load_model(self.model, self.temperature)
        
    
    @staticmethod
    def load_model(model, temperature):
        return ChatOpenAI(
            model=model, 
            temperature=temperature,
            verbose=True)
    

    def process_chat(self, prompt, user_input, session_id, session_history):
        rag_chain = create_rag_chain(prompt, self.llm, self.retriever)
        conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history=session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer"
    )

        response = conversational_rag_chain.invoke({
            "input": user_input},
            config={"configurable": {"session_id": session_id}}
            )

        return response['answer']