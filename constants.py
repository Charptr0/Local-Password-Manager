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
6. Change master password
7. Log out/Back to main menu
8. Exit program (Use this to exit program)
Input: '''

NEW_ENTRY_PROMPT = '''=======================================
Enter a new entry to the database
======================================='''

ENTRY_NAME_PROMPT = '''Type !q to terminate the process
Name of the entry: '''
ENTRY_PASSWORD_PROMPT = '''Password: '''
NEW_ENTRY_NOTES_PROMPT = '''Additional notes (Optional): '''

CHANGE_MASTER_PASSWORD_PROMPT = '''=======================================
Change Master Password
======================================='''

OLD_PASSWORD_PROMPT = '''Type !q to terminate the process
Old Password: '''

DELETE_ENTRY_PROMPT = '''=======================================
Delete an entry from the database
======================================='''

CHANGE_ENTRY_PROMPT = '''=======================================
Change an entry from the database
======================================='''

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
ERR_ENTRY_DNE = 4

#user's main menu enums
GET_PASSWORD = 1
ENTER_NEW_ENTRY = 2
GET_ALL_ENTRY = 3
DELETE_ENTRY = 4
CHANGE_ENTRY = 5
CHANGE_MASTER_PASSWORD = 6
LOG_OUT = 7
EXIT_PROGRAM = 8

##############################################################################################################
#all collections of users
LOGIN_DATABASE_NAME = "logins"