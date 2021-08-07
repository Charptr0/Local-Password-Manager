import database
from writeFile import *
from constants import *

def terminateProgram(user_input): return user_input == "!q"

def mainMenu():
    print(MAIN_MENU_PROMPT)
    user_choice = input(MAIN_MENU_PROMPT)

    try: return int(user_choice)
    except: return -1

def masterLogin():
    print(MAIN_MENU_PROMPT)
    input_username = input(MAIN_LOGIN_USERNAME_PROMPT)

    if(terminateProgram(input_username)): return

    input_password = input(MAIN_LOGIN_PASSWORD_PROMPT)

    if(terminateProgram(input_password)): return


if __name__ == "__main__":
    
    while True:


        masterLogin()
    
