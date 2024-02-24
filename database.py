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

    def get_data_from_db(self, user_id):
        self.cursor.execute(f'SELECT message_id, answer FROM messages_history WHERE user_id = {user_id}')
        return self.cursor.fetchall()

    def insert_data_into_db(self, data):  # data is a list of tuples: [(user_id, message_id, answer), (user_id, message_id, answer), (user_id, message_id, answer)]
        self.connect()
        for i in data:
            self.cursor.execute(f'INSERT INTO messages(user_id, message_id, answer) VALUES {i}')
        self.disconnect()