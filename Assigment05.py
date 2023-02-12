# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# IMarshall,2.11.23,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
strTask = ""  # A task entered by user
strPri = ""  # A Priority assigned by user
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
try:
    objFile = open('ToDoList.txt', 'r')
    for row in objFile:
        lstRow = row.split(',')
        dicRow = {'Task': lstRow[0].strip(), 'Priority': lstRow[1].strip()}
        lstTable += [dicRow]
    objFile.close()
    print('Task:'.ljust(40) + 'Priority:')
    for row in lstTable:
        print(row['Task'].ljust(40) + row['Priority'])
    print('^Data currently in file')
# Double print lstTable, investigate later
except:
    print('''
        Attempted to continue data entry from file.
        No file exists, a new file will be created when you save
        ''')

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        print('The current data is: ')
        print('Task:'.ljust(40) + 'Priority:')
        for row in lstTable:
            print(row['Task'].ljust(40) + row['Priority'])
# Print's in a user friendly format while reminding user of dictionary headers
        input('Press ENTER to continue')
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        print('Type in a task and priority from 1 (low) to 5 (high)')
        strTask = str(input('Enter a task: ').strip())
        while True:
            try:
                strPri = str(input('Enter a priority: '))
            except ValueError:
                print('Please enter a valid integer between 1-5')
                continue
            if (strPri == '1'):
                break
            elif (strPri == '2'):
                break
            elif (strPri == '3'):
                break
            elif (strPri == '4'):
                break
            elif (strPri == '5'):
                break
            else:
                print('Please enter a value between 1 and 5')
                # Holds user to defined priority range
        dicRow = {'Task': strTask, 'Priority': strPri}
        lstTable += [dicRow]
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        strTask = str(input('What task would you like to remove? '))
        for row in lstTable:
            if row['Task'].lower() == strTask.lower():
                lstTable.remove(row)
                print('row removed')
                break
                # Without break statement will print for every row in instead of single message
            else:
                print('data not found in row')
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open('ToDoList.txt', 'w')
        for row in lstTable:
            objFile.write(str(row['Task']) + ',' + str(row['Priority']) + '\n')
        objFile.close()
        print(' Data was saved to file')
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print('''
            Thank you for using our services.
            Have a nice day
            ''')
        break  # and Exit the program
