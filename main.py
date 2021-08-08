import database
from writeFile import *
from constants import *

def terminateProgram(user_input): 
    if user_input == "!q":
        print("The process has been terminated\n")
        return True
    
    return False

def errorHandling(err_code):
    if err_code == ERR_INVALID_USERNAME: print("The Username does not exist, please try again\n")
    elif err_code == ERR_INVALID_PASSWORD: print("The password does not match this username, please try again\n")
    elif err_code == ERR_USERNAME_ALREADY_EXIST: print("This username already exist, please try again\n")
    else: return

def mainMenu():
    print(MAIN_MENU_PROMPT)
    user_choice = input(MAIN_MENU_CHOICES)

    try: return int(user_choice)
    except: return -1

def masterLogin():
    print(MAIN_MENU_PROMPT)
    input_username = input(MAIN_LOGIN_USERNAME_PROMPT)

    if(terminateProgram(input_username)): return

    input_password = input(MAIN_LOGIN_PASSWORD_PROMPT)

    if(terminateProgram(input_password)): return

    (isValid, err) = database.isValidLogin(input_username, input_password)

    if err != NO_ERR: errorHandling(err)




if __name__ == "__main__":
    database.init()
    
    while True:
        main_choice = mainMenu()

        if main_choice == MAIN_MENU_LOGIN: masterLogin()
        elif main_choice == MAIN_MENU_CREATE_NEW_USER: pass
        elif main_choice == MAIN_MENU_DELETE_USER: pass
        elif main_choice == MAIN_MENU_QUIT: break
        else: print(UNKNOWN_CHOICE_ERR)
    
