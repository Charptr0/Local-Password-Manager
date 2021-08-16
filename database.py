import sqlite3
import os
from sqlite3.dbapi2 import Error
from constants import *
from datetime import datetime

LOGIN_PATH = "users/" + LOGIN_DATABASE_NAME + ".db"

def getCurrentTime(): return datetime.today().strftime('%Y-%m-%d')

def init():
    if not os.path.exists("users/"): os.makedirs("users/") #create the user/ dir if not exist
    if not os.path.exists("output/"): os.makedirs("output/") #create the output/ dir if not exist

    #secure a connection to the database
    connection = sqlite3.connect(LOGIN_PATH)
    cursor = connection.cursor()

    try: #try to create the table
        cursor.execute('''CREATE TABLE IF NOT EXISTS users(
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            date_of_creation TEXT NOT NULL
        )''')

        connection.commit()

    except Error as e: print(e) #if err
    finally: connection.close() #close the connection

#check if the input username and password matches the record in the database
def isValidLogin(input_username, input_password):
    connection = sqlite3.connect(LOGIN_PATH)
    cursor = connection.cursor()

    try: #check for username
        cursor.execute('''SELECT username, password FROM users WHERE username="{}"'''.format(input_username))
        user = cursor.fetchall()
    except Error as e: print(e)
    finally: connection.close()
    
    if len(user) == 0: return ERR_INVALID_USERNAME #no such username exist
    if user[0][1] != input_password: return ERR_INVALID_PASSWORD #password does not match

    return NO_ERR

def addNewLogin(input_username, input_password):
    connection = sqlite3.connect(LOGIN_PATH)
    cursor = connection.cursor()

    try:
        cursor.execute('''SELECT username FROM users WHERE username="{}"'''.format(input_username))
        data = cursor.fetchall()
    except Error as e: print(e)

    if len(data) > 0: 
        connection.close()
        return ERR_USERNAME_ALREADY_EXIST

    try:
        cursor.execute('''INSERT INTO users(username, 
        password, 
        date_of_creation) VALUES (?, ?, ?)''', [input_username, input_password, getCurrentTime()])

        connection.commit()
    except Error as e: print(e)
    finally: connection.close()

    connection = sqlite3.connect("users/" + input_username + ".db")
    cursor = connection.cursor()

    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS entries(
            name TEXT NOT NULL,
            password TEXT NOT NULL,
            notes TEXT)
            ''')

        connection.commit()
        print("Entry has been successfully added to the database\n")
    except Error as e: print(e)
    finally: connection.close()

    return NO_ERR

def deleteUserFromDatabase(username):
    connection = sqlite3.connect(LOGIN_PATH)
    cursor = connection.cursor()

    try:
        cursor.execute('''DELETE FROM users WHERE username="{}"'''.format(username))
        connection.commit()
        print("Entry has been successfully deleted from the database\n")
    except Error as e: print(e)
    finally: connection.close()

def getAllEntries(username):
    connection = sqlite3.connect("users/ " + username + "db")
    cursor = connection.cursor()

    data = []
    
    try:
        cursor.execute('''SELECT name,password,notes FROM entries''')
        data = cursor.fetchall()
    except Error as e: print(e)
    finally: connection.close()

    return data