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

LOGIN_USERNAME_PROMPT = '''Type "!q" to terminate the process
Master Username: '''

LOGIN_PASSWORD_PROMPT = '''Master Password: '''

ADD_USER_PROMPT = '''=======================================
Add a user to the database
======================================='''

ADD_USER_USERNAME_PROMPT = '''Type !q to terminate the process
New Username: '''

ADD_USER_PASSWORD_PROMPT = '''New Password: '''

DELETE_USER_PROMPT = '''=======================================
Delete a user from the database
======================================='''

LOGIN_USER_CHOICES = '''1. Get a password
2. Enter a new entry
3. Get all entry
4. Delete an entry
5. Change an entry
6. Change Password
7. Log out/Back to main menu
Input: '''

NEW_ENTRY_PROMPT = '''=======================================
Enter a new entry to the database
======================================='''

NEW_ENTRY_NAME_PROMPT = '''Type !q to terminate the process
Name of the entry: '''
NEW_ENTRY_PASSOWRD_PROMPT = '''Password: '''
NEW_ENTRY_NOTES_PROMPT = '''Additional notes (Optional): '''

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

#user's main menu enums
GET_PASSWORD = 1
ENTER_NEW_ENTRY = 2
GET_ALL_ENTRY = 3
DELETE_ENTRY = 4
CHANGE_ENTRY = 5
CHANGE_MASTER_PASSWORD = 6
LOG_OUT = 7

##############################################################################################################
#all collections of users
LOGIN_DATABASE_NAME = "logins"