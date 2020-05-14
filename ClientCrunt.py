# --CLIENT--
from os import system, name  # import only system from os
import xmlrpc.client
import json

def main():
    # Magic Numbers
    student = 1
    staff = 2
    quit = 3
    addStudentResuts = 1
    showHonours = 2
    showTScript = 3
    correctStudentIdLength = 8
    correctStaffIdLength = 8

    clear()
    while True:
        clear()
        selection = marksAutoMenu("Welcome to the Blah CLIENT System\nPlease select a Student login or a Staff login",
                                  ["Student Login", "Staff Login", "Quit"])
        if int(selection) == student:
            studentID = getId("Student", correctStudentIdLength)
            if (studentID != "quit"):
                print("The student ID is: " + studentID)
                print("VALIDATING")
                detail = {"studentID": studentID} # Create Dictionary
                payload = json.dumps(detail, indent = 4) # Convert Dict to json
                print(payload)
                valid = validateStudent(payload) # TODO - Call for validation at Server End.
                # TODO - If valid CALL get results from Server END
                # TODO - Print Results (Nice Table, enter to continue)
                # TODO return to START!
                print("TODO - RPC\nPress Enter to continue")
                input()
            else:
                print("User selected Quit from the menu")

        elif int(selection) == staff:
            staffID = getId("Staff", correctStaffIdLength)
            if (staffID != "quit"):
                print("The Staff ID is: " + staffID)
                print("VALIDATING")
                detail = {"staffID": staffID} # Create Dictionary
                payload = json.dumps(detail, indent = 4) # Convert Dict to json
                print(payload)
                valid = validateStaff(payload) # TODO - Call for validation at Server End. returns True for debug.

                if valid: # TODO - If valid CALL get results from Server END
                    while True:
                        print("Welcome\nPlease Enter a Student ID to search")
                        studentID = getId("Student", correctStudentIdLength)
                        if (studentID != "quit"):
                            print("The student ID is: " + studentID)
                            print("VALIDATING")
                            detail = {"studentID": studentID} # Create Dictionary
                            payload = json.dumps(detail, indent = 4) # Convert Dict to json
                            print(payload)
                            valid = validateStudent(payload) # TODO - Call for validation at Server End. returns True for debug

                            if valid: # TODO - If valid CALL get results from Server END
                                dummyPayload = [{'studentID': 12312312, 'studentName': 'mark joyce'}] # Pretend return message, debugging.
                                table_list(dummyPayload)
                                selection = marksAutoMenu("Welcome to the student results menu, please make a selection",
                                                          ["Enter student results", "Check for Honours Eligibility",
                                                           "Show T-Script", "Quit"])
                                print("You selected: " + selection) # Debug
                                # TODO - PreProcessing and RPC CALLS
                                if selection == addStudentResuts:
                                    pass # Create payload and send it.
                                elif selection == showHonours:
                                    pass # Receive List, or Dict, or JSON.
                                elif selection == showTScript:
                                    pass # Receive List, or Dict, or JSON.
                                elif selection == quit + 1:
                                    break
                                break # TODO -Remove, for debug. See above pass statements.
                            else:
                                print("Student ID is invalid, press Enter to continue")
                                input()

                            print("TODO - RPC\nPress Enter to continue") # Reminder, REMOVE
                            input()
                        else:
                            print("User selected quit from the menu") # Debug
                            break
                else:
                    print("ERROR, check connection / ID invalid")
            else:
                print("User selected quit from the menu") # Debug
        elif int(selection) == quit:
            print("Goodbye")
            break


def table_list(value_list):
    # Print the table
    print ("%5s %13s" % ("-" * 12, "-" * 14))
    print ("%5s %15s" % ("Student ID", "Student Name"))
    print ("%5s %13s" % ("-" * 12, "-" * 14))
    for node in range(len(value_list)):
        print ("%6s %16s" % (value_list[node]['studentID'], value_list[node]['studentName']))


# Marks Auto Menu
# Prompt = Greeting
# menuList = Menu items in list form.
def marksAutoMenu(prompt, menuList):
    print(prompt)
    while True:
        menuLimit = len(menuList)
        for i in range(menuLimit):
            print("" + str(i + 1) + ") " + menuList[i] )
        selection = input()
        print("You Selected: " + selection)
        if numericAndInRange(selection, menuLimit):
            print("You selected a valid option")
            break
        else:
            print("You selected a invalid option, press enter to continue")
            input()
            clear()
    return selection


# Get the student / staff ID
# Returns valid ID.
def getId(type, correctIdLength):
    while True:
        print(type + " IDs have " + str(correctIdLength) + " digits")
        iD = input("Enter "+ type + " ID (quit to exit): ")
        if iD.isdecimal():
            idLength = len(iD)
            if idLength == correctIdLength:
                break
            else:
                print("ID is of incorrect length, try again")
        else:
            if iD == "quit":
                break
            else:
                print("please enter a numeric " + type + " id")
    return iD


def rpcTester():
    with xmlrpc.client.ServerProxy("http://10.1.1.76:1234/") as proxy:
        if proxy.does_it_work():
            print("It works")
        else:
            print("Oh shit it didn't")


# Clear Console Function
def clear():
    # for windows
    if name == 'nt':
        system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')


# Check valueTocheck For number and range.
def numericAndInRange(valueToCheck, range):
    if valueToCheck.isnumeric():
        if 0 < int(valueToCheck) <= range:
            return True
        else:
            return False
    else:
        return False


# HERE IS WHERE THE RPCs WILL GO
# Validate the student ID.
def validateStudent(studentID):
    # TODO sends ID to server for validation, returns true or false.? I guess
    #pass  # stub
    return True

# Validate the staff ID.
def validateStaff(staffID):
    # TODO sends ID to server for validation, returns true or false.? I guess
    return True # stub

def showHonours(studentID):
    pass

def addResults(studentID, unit, result):
    pass

def showTScript(studentID):
    pass

main()
