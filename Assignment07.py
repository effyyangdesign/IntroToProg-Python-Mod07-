# ------------------------------------------------- #
# Title: Assignment07
# Description: A simple example of storing data in a binary file and exception handling
# Yizhou yang, 08.23.2020,Edited Script
# ------------------------------------------------- #

import pickle

# Data -------------------------------------------- #
file_name = 'Appointment.dat'
lstCustomer = []
tableCustomer = []
totalLst = []
loadlst=[]
idInput =""
nameInput=""
strChoice = ""

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name, "ab")
    pickle.dump(totalLst, objFile)
    objFile.close()



def read_data_from_file(file_name):

    try:
        objFile = open("Appointment.dat","rb")

    except FileNotFoundError as error:
        print("No appointment document was found. ")

    try:
        while True:
            tableCustomer = pickle.load(objFile)
            if len(tableCustomer) > 0:
                totalLst.append(tableCustomer)
                print(tableCustomer)
                objFile.close()
            else:
                continue

    except EOFError as e:
        print("This is the end of the appointment list.")
    except Exception as e:
        print("Generic Error")





def print_menu_Tasks():
    print('''
    Menu of Options
    1) Add new appointment
    2) Show existing appointment 
    3) Exit
    ''')
    print()  # Add an extra line for looks


def add_appointment():
    totalLst.clear()
    nameInput = input("Please Enter Customer's name: ")
    dateInput = input("Please Enter appointment time (in mmdd format): ")
    try:
        if len(dateInput)> 4:
                raise Exception ('Please enter a valid date in correct format. ')
    except Exception as e:
        print(e)
    dicRow = {"Customer": nameInput, "Date":dateInput,}
    totalLst.append(dicRow)
    save_data_to_file(file_name,totalLst)

#
# def delete_appointment():
#
#     deleteInput = input("Which appointment would you like to delete (by customer\'s name)? ")
#     obj_file = open("Appointment.dat", "rb")
#     while True:
#         try:
#             loadlst = pickle.load(obj_file)
#             for i in range(len(loadlst)):
#                 if loadlst[i]["Customer"] == deleteInput:
#                     del loadlst[i]
#                 else:
#                     totalLst.append(loadlst)
#         except EOFError as e:
#             break
#     print(totalLst)




# def save_exit(file_name, list_of_data):
#     objFile = open(file_name, "wb")
#     pickle.dump(totalLst, objFile)
#     objFile.close()



# Presentation ------------------------------------ #

# Get name and time From user, then store it in a list object


while (True):

    print_menu_Tasks()
    strChoice = input("Please select an option: ")

    if strChoice == '1':  # Add new appointment
        add_appointment()
        continue  # to show the menu

    # elif strChoice == '2':  # Remove an existing appointment
    #     delete_appointment()
    #     # save_data_to_file(file_name,tableCustomer)
    #     continue  # to show the menu

    elif strChoice == '2':  # Show existing appointments
        read_data_from_file(file_name)
        continue  # to show the menu

    elif strChoice == '3':  # Save and Exit
        # save_exit(file_name,totalLst)
        print ("Goodybye!")
        break



