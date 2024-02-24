from dotenv import load_dotenv
from data_processor import *
from database import *
import os

class GeneralController:
    database = None
    data_processor = None

    def __init__(self):
        load_dotenv()
        database_path = os.getenv('DATABASE_PATH')
