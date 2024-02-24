import sqlite3


class Database:
    connection = None
    cursor = None
    path = ''

    def __init__(self, path):
        self.path = path

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
        self.cursor.execute(f'INSERT INTO messages_history(chat_id, message_id, answer, role) VALUES {(chat_id, message_id, text, role)}')
        self.disconnect()
