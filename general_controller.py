from dotenv import load_dotenv
from data_processor import *
from database import *
import os
import openai


class GeneralController:
    database = None
    data_processor = None
    engine = None

    def __init__(self):
        load_dotenv()
        self.engine = os.getenv('CHATGPT_ENGINE')
        openai.api_key = os.getenv('OPEN_AI_TOKEN')
        database_path = os.getenv('DATABASE_PATH')
        self.database = Database(database_path)

    @staticmethod
    def get_tg_token():
        return os.getenv('TG_TOKEN')

    def get_ai_message(self, chat_id, text):
        responce = openai.Completion.create(
            engine=self.engine,
            prompt=text,
            max_tokens=2048
        )
        return responce
