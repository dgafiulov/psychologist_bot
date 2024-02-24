from dotenv import load_dotenv
import data_processor
from database import *
import os
from openai import OpenAI
from ai_contact import *
import datetime


class GeneralController:
    database = None
    data_processor = None
    engine = None
    ai = None

    def __init__(self):
        load_dotenv()
        self.engine = os.getenv('CHATGPT_ENGINE')
        self.ai = AI(OpenAI())
        database_path = os.getenv('DATABASE_PATH')
        self.database = Database(database_path)

    @staticmethod
    def is_valid_date(date_string):
        try:
            datetime.datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    @staticmethod
    def get_tg_token():
        return os.getenv('TG_TOKEN')

    @staticmethod
    def get_tg_admin_token():
        return os.getenv('TG_TOKEN_ADMIN')

    def get_amount_of_users(self, date=None):
        if date is None:
            return self.database.get_amount_of_user()
        else:
            try:
                return self.database.get_amount_of_user(date)
            except:
                return -1

    def get_ai_message(self, chat_id, text):
        self.database.insert_data_into_db(chat_id, text, 'user', self.get_date())
        message_history = self.database.get_data_from_db(chat_id)
        message_history = data_processor.edit_data(message_history)
        ai_answer = self.ai.get_answer(self.engine, message_history).choices[0].message.content
        self.database.insert_data_into_db(chat_id, ai_answer, 'system', self.get_date())
        return ai_answer
