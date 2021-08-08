import sqlite3
import os
from sqlite3.dbapi2 import Error, connect
from constants import *

LOGIN_PATH = "users/" + LOGIN_DATABASE_NAME + ".db"

def init():
    if not os.path.exists("users/"): os.makedirs("users/")

    connection = sqlite3.connect(LOGIN_PATH)
    cursor = connection.cursor()

    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS users(
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            date_of_creation TEXT NOT NULL
        )''')

        connection.commit()

    except Error as e: print(e)
    finally: connection.close()

def isValidLogin(input_username, input_password):
    connection = sqlite3.connect(LOGIN_PATH)
    cursor = connection.cursor()

    try:
        cursor.execute('''SELECT username, password FROM users WHERE username="{}"'''.format(input_username))
        user_username = cursor.fetchall()
    except Error as e: print(e)
    
    if len(user_username) == 0: return False, ERR_INVALID_USERNAME
    if len(user_username) > 1: return False, ERR_USERNAME_ALREADY_EXIST

    try:
        cursor.execute('''SELECT username, password FROM users WHERE password="{}"'''.format(input_password))
        user_password = cursor.fetchall()
    except Error as e: print(e)

    if len(user_password) == 0: return False, ERR_INVALID_PASSWORD

    connection.close()

    return True, NO_ERR

init()