#titles and prompts
MAIN_MENU_PROMPT = '''=======================================
Local Password Manager
======================================='''

MAIN_MENU_CHOICES = '''1. Login
2. Create a new user
3. Delete a user
4. Quit
Input: '''

UNKNOWN_CHOICE_ERR = "Unknown choice, please try again\n"

MAIN_LOGIN_USERNAME_PROMPT = '''Type "!q" to terminate the process
Master Username: '''

MAIN_LOGIN_PASSWORD_PROMPT = '''Master Password: '''

ADD_USER_PROMPT = '''=======================================
Add a user to the database
======================================='''

ADD_USER_USERNAME_PROMPT = '''Type !q to terminate the process
New Username: '''

ADD_USER_PASSWORD_PROMPT = '''New Password: '''

##############################################################################################################
#enums for main menu choices
MAIN_MENU_LOGIN = 1
MAIN_MENU_CREATE_NEW_USER = 2
MAIN_MENU_DELETE_USER = 3
MAIN_MENU_QUIT = 4

#Error code enums
NO_ERR = 0
ERR_INVALID_USERNAME = 1
ERR_INVALID_PASSWORD = 2
ERR_USERNAME_ALREADY_EXIST = 3

##############################################################################################################
#all collections of users
LOGIN_DATABASE_NAME = "logins"