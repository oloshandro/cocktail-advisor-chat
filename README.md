## **Description**
This project is a chat-based cocktail advisor that leverages an LLM-powered chatbot to answer users' questions about cocktails. The chatbot integrates a vector database to store cocktail knowledge, improving recommendations with RAG (Retrieval-Augmented Generation).


## **Features Implemented**

✅ **Flask API Endpoints:** Provides endpoints for generating data and interacting with the chatbot.

✅ **Chat Interface:** A web-based chat interface where users can ask cocktail-related questions.

✅ **LLM Integration:** OpenAI GPT-4 processes user queries and provides responses.

✅ **Vector Database:** FAISS stores cocktail information and user preferences for better retrieval.

✅ **Retrieval-Augmented Generation (RAG):** Enhances LLM responses with structured cocktail knowledge.


# **Installation & Setup**

**1 Clone the Repository**

`git clone https://github.com/yourusername/cocktail-advisor-chat.git
cd cocktail-advisor-chat`

**2 Install Dependencies**

`pip install -r requirements.txt`

**3 Set Up Environment Variables**

Create a `.env` file in the root directory and add your OpenAI API key:

`OPENAI_API_KEY=your-openai-api-key`

**4 Run the Application**

Run Flask Application

`python run.py`


## **Next Steps & TODO**

 **Debugging:** Fix minor issues in API and chat interface.

 **Output Formatting:** Improve the chatbot's response visualization for better readability.

 **Prompt Engineering:** Fine-tune prompts for more accurate LLM responses.🔬
 
 **RAG Testing:** Validate and optimize retrieval-augmented generation for cocktail data.

 **User Preferences Storage:** Implement detecting and storing user-related data