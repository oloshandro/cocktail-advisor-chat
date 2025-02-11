import os

class Config:
    APP_DIR = os.path.abspath(os.curdir)
    WORK_DIR = os.path.join(os.sep, APP_DIR, "app").lstrip(os.sep)
    RAG_DIR = os.path.join(os.sep, WORK_DIR, "knowledge").lstrip(os.sep)
    VECTORSTORE_PATH = os.path.join(os.sep, RAG_DIR, "vectorstore").lstrip(os.sep)

    DATA_FILE_NAME = f"final_cocktails.csv"
    DATA_PATH =  os.path.join(os.sep, RAG_DIR, DATA_FILE_NAME).lstrip(os.sep)



    OPENAI_MODEL = 'gpt-4o'
    TEMPERATURE = 0.7
