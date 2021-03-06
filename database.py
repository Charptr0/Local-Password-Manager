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

def enterNewEntries(username, name, password, notes):
    connection = sqlite3.connect("users/" + username + ".db")
    cursor = connection.cursor()

    try:
        cursor.execute('''INSERT INTO entries(name, password, notes) VALUES (?,?,?)''', [name, password, notes])
        connection.commit()
        print("Entry has been successfully added from the database\n")
    except Error as e: print(e)
    finally: connection.close()

def getAllEntries(username):
    connection = sqlite3.connect("users/" + username + ".db")
    cursor = connection.cursor()
    
    try:
        cursor.execute('''SELECT name,password,notes FROM entries''')
        return cursor.fetchall()
    except Error as e: print(e)
    finally: connection.close()

def getPassword(username, entry_name):
    connection = sqlite3.connect("users/" + username + ".db")
    cursor = connection.cursor()

    data = []
    
    try:
        cursor.execute('''SELECT password,notes FROM entries WHERE name="{}"'''.format(entry_name))
        data = cursor.fetchall()
    except Error as e: print(e)
    finally: connection.close()

    return data

def changeMasterPassword(username, new_password):
    connection = sqlite3.connect(LOGIN_PATH)
    cursor = connection.cursor()

    try:
        cursor.execute('''UPDATE users SET password="{}" WHERE username="{}"'''.format(new_password, username))
        connection.commit()
        print("Successfully updated password\n")
    except Error as e: print(e)
    finally: connection.close()

#check if the given name exist in the database
def validName(username, name):
    connection = sqlite3.connect("users/" + username + ".db")
    cursor = connection.cursor()

    try:
        cursor.execute('''SELECT * FROM entries WHERE name="{}"'''.format(name))
        data = cursor.fetchall()
        if len(data) != 0: return True 
        else: return False

    except Error as e: print(e)
    finally: connection.close()

#delete an entry from the database
def deleteEntry(username, name):
    connection = sqlite3.connect("users/" + username + ".db")
    cursor = connection.cursor()

    try:
        cursor.execute('''DELETE FROM entries WHERE name="{}"'''.format(name))
        connection.commit()
        print("Successfully deleted entry from the database\n")
    except Error as e: print(e)
    finally: connection.close()

#change the password of a given entry
def changeEntry(username, name, new_password):
    connection = sqlite3.connect("users/" + username + ".db")
    cursor = connection.cursor()

    try:
        cursor.execute('''UPDATE entries SET password={} WHERE name="{}"'''.format(new_password, name))
        connection.commit()
        print("Successfully changed the entry from the database\n")
    except Error as e: print(e)
    finally: connection.close()