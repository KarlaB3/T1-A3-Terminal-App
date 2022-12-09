#upon executing the program users enter their entries then it prompts them to save to existing diary or create a new diary from the list they've created. BUT THEN the initial options won't have an edit function? or it can, because it prompts the user to edit the list that's  just been entered. but if they want to view entries,...it will come up as a prettytABLE IN the terminal with just today's entries and if they want to view more they'll have to export? which will then prompt them to either enter diary name or create new diary to export.

print("Welcome to your personalised food diary. \nUse this program to track what you eat for breakfast, lunch, dinner and snacks each day. \nView the available options below, and when prompted enter your selection from the available options.")
def initial_options():
    print("1: Open Existing Diary")
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
    # prompt user to enter weekly gluten limit (as integer)

def new_diary():
    diary_name = input("Create a new diary. Please enter a diary name that is maximum 6 characters long  ")
    if diary_name = #exists open that file
    elif diary_name = #doesn't exist create new file

#registered diary flow - enter profile name and see options
# def registered_user():
    # get the user's input of their profile name
    # check the current directory to see if that profile name i.e. file name exists
def existing_diary():
    existing_confirmed = input("Open your diary by entering the diary name: ")
    if existing_confirmed == #exists, open file
    elif existing_confirmed != #doesn't exist:
        print("Your diary name isn't recognised. Please try again.")  
        initial_options()
        initial_selections()
    




    


#
