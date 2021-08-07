import sqlite3
from sqlite3.dbapi2 import Error
from constants import *

LOGIN_PATH = "users/" + LOGIN_DATABASE_NAME + ".db"

def init():
    connection = sqlite3.connect(LOGIN_PATH)
    cursor = connection.cursor()

    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS users(
            username TEXT NOT NULL,
            pasword TEXT NOT NULL,
            date_of_creation TEXT NOT NULL
        )''')

        connection.commit()

    except Error as e: print(e)
    finally: connection.close()

def isValidLogin(input_username, input_password):
    pass


init()