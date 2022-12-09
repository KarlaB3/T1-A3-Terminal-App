#upon executing the program users are prompted to either access an existing diary or create a new diary.

#OR give users the option first off...i.e. welcome to food diary. enter selection below. i.e. the users can enter their entries then it prompts them to save to existing diary or create a new diary from the list they've created. 

print("Welcome to your personalised food diary. \nUse this program to track what you eat for breakfast, lunch, dinner and snacks each day. \nView the available options below, and when prompted enter your selection from the available options.")
def initial_options():
    print("1: Access Existing Diary")
    print("2: Create New Diary")

def initial_selections():
    confirmation_input = input("Please enter the number that corresponds with your selection: ")
    if confirmation_input == "1":
        existing_confirmed = input("Open your diary by entering the diary name: ")
    elif confirmation_input == "2":
        new_confirmed = input("Create a new diary. Please enter a diary name that is maximum 6 characters long  ")
    elif (confirmation_input != "1") or (confirmation_input != "2"):
        print("What you've selected isn't recognised. Please try again.")
        initial_options()
        initial_selections()

initial_options()
initial_selections()



#new diary flow - create new diary and see options
# def new_diary():
    # get the user's input of their profile name. Ensure it is within the correct parameters (should there be parameters?)
    # save the diary name as the name of the .csv file. In Pandas, you create individual DataFrames per diary and save in .csv format.   ``` import pandas as pd

def new_diary():
    diary_name = input("Create a new diary. Please enter a diary name that is maximum 6 characters long  ")
    print("Thank you, confirming your diary name is" + diary_name)

#registered diary flow - enter profile name and see options
# def registered_user():
    # get the user's input of their profile name
    # check the current directory to see if that profile name i.e. file name exists
def existing_diary():
    existing_confirmed = input("Access your diary by entering the diary name: ")
    if existing_confirmed == #exists, open file
    elif existing_confirmed != #doesn't exist:
        print("Your diary name isn't recognised. Please try again.")  
        initial_options()
        initial_selections()

    #try:
	#f = open(“requirement.txt”, mode=’w’)
	#f.write(“enter the text you want to write to the file”)
	f.close() → closes the file once complete
except FileNotFoundError:
	print(‘please enter correct file path’)   → exception handling if the file isn’t found
else:
	print(‘file detected’)

    




    


#
