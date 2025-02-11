from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv, find_dotenv
import os
from app.llm.chat import CocktailChat
from app.llm.prompt_helpers import prompt, create_rag_chain
from config import Config
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory


_ = load_dotenv(find_dotenv())
api_key=os.environ.get("OPENAI_API_KEY")
# llm = OpenAI()
config = Config()
connector = CocktailChat(config.DATA_PATH, config.VECTORSTORE_PATH, config.OPENAI_MODEL, config.TEMPERATURE)
connector.initialize()
store = {}

###################################################

app = Flask(__name__, template_folder="app/templates")

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/generate", methods=['POST'])
def get_bot_response():

    data = request.json
    user_text = data.get('msg')

    try:
        text_response = generate_text_response(user_text)
    except Exception as e:
        text_response = str(e)


    return jsonify({"response": text_response})


def generate_text_response(user_input):
    data = request.json
    session_id = data.get("session_id", "default_session")
    session_history = get_session_history
    
    response = connector.process_chat(prompt, user_input, session_id, session_history)
    print(response)
    return response


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


if __name__ == '__main__':
    app.run()