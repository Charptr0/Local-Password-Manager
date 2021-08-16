import random

def generateID():
    id = "r"
    for i in range(9):
        id += str(random.randint(0,9)) 

    return id

def writeAllEntries(entries):
    NAME = 0
    PASSWORD = 1
    NOTES = 2

    requestFileName = generateID()

    data = "Getting all entries in the database\n"

    if len(entries) == 0:
        with open("output/" + requestFileName + ".txt", "w") as f:
            data += "The database is empty\n"
            f.write(data)
    else:
        with open("output/" + requestFileName + ".txt", "w") as f:
            for i in range(len(entries)):
                data += entries[i][NAME] + "\t" + entries[i][PASSWORD] + "\t" + entries[i][NOTES]

            f.write(data)

    print("Your request is in Output/{}.txt".format("requestFileName"))
