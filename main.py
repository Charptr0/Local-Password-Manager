import database
from writeFile import *
from constants import *

#if the user enter "!q" return true to terminate the current process
def terminateProgram(user_input): 
    if user_input == "!q":
        print("The process has been terminated\n")
        return True
    
    return False

#Error handling, if any of the err code hit these values, terminate the current process and print the err message
def errorHandling(err_code):
    if err_code == ERR_INVALID_USERNAME: print("The username does not exist, please try again\n")
    elif err_code == ERR_INVALID_PASSWORD: print("The password does not match this username, please try again\n")
    elif err_code == ERR_USERNAME_ALREADY_EXIST: print("This username already exist, please try again\n")
    else: return

#print the main menu and show all main menu choices
#return the choice that was made by the user
def mainMenu():
    print(MAIN_MENU_PROMPT)
    user_choice = input(MAIN_MENU_CHOICES)

    try: return int(user_choice) #try to return the selection as an int
    except: return -1 #cannot change to int, return a invalid option

def masterLogin():
    print(MAIN_MENU_PROMPT)
    input_username = input(MAIN_LOGIN_USERNAME_PROMPT)

    if terminateProgram(input_username): return #check for "!q"

    input_password = input(MAIN_LOGIN_PASSWORD_PROMPT)

    if terminateProgram(input_password): return #check for "!q"

    error = database.isValidLogin(input_username, input_password)

    if error != NO_ERR: errorHandling(error)
    else: print("yes")

#add a new user to the database
def addUser():
    print(ADD_USER_PROMPT)
    new_username = input(ADD_USER_USERNAME_PROMPT) #ask for the new username

    if terminateProgram(new_username): return #check for "!q"

    new_password = input(ADD_USER_PASSWORD_PROMPT) #ask for the new password

    if terminateProgram(new_password): return

    err = database.addNewLogin(new_username, new_password) #check for err when adding to the database

    if err != NO_ERR: errorHandling(err) #if something went wrong

#Main program
if __name__ == "__main__":
    database.init() #initialize the database

    while True:
        main_choice = mainMenu() 

        if main_choice == MAIN_MENU_LOGIN: masterLogin()
        elif main_choice == MAIN_MENU_CREATE_NEW_USER: addUser()
        elif main_choice == MAIN_MENU_DELETE_USER: pass
        elif main_choice == MAIN_MENU_QUIT: break
        else: print(UNKNOWN_CHOICE_ERR)