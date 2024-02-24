import sqlite3
import datetime


class Database:
    timezone = datetime.timezone(datetime.timedelta(hours=5))
    connection = None
    cursor = None
    path = ''

    def __init__(self, path):
        self.path = path

    def get_date(self):
        return str(datetime.datetime.now(self.timezone).date())

    def connect(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.connection.commit()
        self.connection.close()

    def get_last_message_id(self, chat_id):
        self.cursor.execute(f'SELECT MAX(message_id) FROM messages_history WHERE chat_id = {chat_id}')
        max_message_id = self.cursor.fetchall()[0][0]
        if max_message_id is None:
            max_message_id = -1
        return max_message_id

    def get_data_from_db(self, chat_id):
        self.connect()
        self.cursor.execute(f'SELECT message_id, answer, role FROM messages_history WHERE chat_id = {chat_id}')
        data = self.cursor.fetchall()
        self.disconnect()
        return data

    def insert_data_into_db(self, chat_id, text, role):
        self.connect()
        message_id = self.get_last_message_id(chat_id) + 1
        self.cursor.execute(f'INSERT INTO messages_history(chat_id, message_id, answer, role, date) VALUES {(chat_id, message_id, text, role, self.get_date())}')
        self.disconnect()

    def get_amount_of_user(self, date=None):
        if date is None:
            date = self.get_date()

        self.connect()
        self.cursor.execute('SELECT COUNT(DISTINCT chat_id) FROM messages_history')
        total_amount = self.cursor.fetchall()
        self.cursor.execute(f'SELECT COUNT(DISTINCT chat_id) FROM messages_history WHERE date = \'{date}\'')
        day_amount = self.cursor.fetchall()

        return {
            'total': total_amount,
            'day': day_amount
        }
