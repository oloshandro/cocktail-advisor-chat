from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import create_retrieval_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain



prompt_template = """
You are a knowledgeable, enthusiastic, and attentive cocktail advisor with expertise in mixology. 
Your goal is to provide accurate, engaging, and creative recommendations for users seeking cocktail suggestions based on ingredients, flavors, and preferences. 
You rely on the provided {context}. Keep your answers concise, helpful, and engaging, while adapting your tone to match the user’s level of expertise—whether they are a beginner or a cocktail enthusiast.
You can ask questions to specify users preferences.
"""


   

prompt = ChatPromptTemplate.from_messages([
    ('system', prompt_template),
    ('system', "Here is some relevant cocktail knowledge: {context}"),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{input}')
])


def create_rag_chain(prompt, llm, retriever):
    chain = create_stuff_documents_chain(
        llm=llm,
        prompt=prompt,
        output_parser = StrOutputParser()
    )

    retriever_prompt = ChatPromptTemplate.from_messages([
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{input}"),
                ("human", "Given the above conversation, react to the user's reply in a friendly manner.")
    ])
    
    history_aware_retriever = create_history_aware_retriever(
        llm=llm,
        retriever=retriever,
        prompt=retriever_prompt
    )

    rag_chain = create_retrieval_chain(history_aware_retriever, chain)
    
    return rag_chain
