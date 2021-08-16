import random
from constants import ERR_ENTRY_DNE, NO_ERR

#generate a random 10 digit string file name
def generateID():
    id = "r"
    for i in range(9):
        id += str(random.randint(0,9)) 

    return id

def writeAllEntries(entries):
    #enums
    NAME = 0
    PASSWORD = 1
    NOTES = 2

    requestFileName = generateID()

    data = "Getting all entries in the database\n"

    if len(entries) == 0: #no entries are found in the db
        with open("output/" + requestFileName + ".txt", "w") as f:
            data += "The database is empty\n"
            f.write(data)
    else:
        with open("output/" + requestFileName + ".txt", "w") as f: #write to file
            for i in range(len(entries)):
                data += entries[i][NAME] + "\t" + entries[i][PASSWORD] + "\t" + entries[i][NOTES]

            f.write(data)

    print("Your request is in Output/{}.txt".format(requestFileName))

def writePassword(entry):
    #enums
    PASSWORD = 0
    NOTES = 1

    if len(entry) == 0: return ERR_ENTRY_DNE #the name DNE in the db

    data = ""
    requestFileName = generateID()

    with open("output/" + requestFileName + ".txt", "w") as f:
        for i in range(len(entry)):
            data += entry[i][PASSWORD] + "\t" + entry[i][NOTES]

        f.write(data)

    print("Your request is in Output/{}.txt".format(requestFileName))
    return NO_ERR