print("Would you like to save today's meals into an existing diary, or create and save a new diary? \nWhen prompted, please enter the number that corresponds with your selection.")

def diary_options():
    print("1: Save to Existing Diary")
    print("2: Create and Save to New Diary")

def diary_selections():
    selection_input = input("Please enter the number that corresponds with your selection: ")
    if selection_input == "1":
        existing_diary()
    elif selection_input == "2":
        new_diary()
    else:
        print("What you've selected isn't recognised. Please try again.")
        diary_options()
        diary_selections()

#created new diary with today's meals
#now I just have to rename the file and append the diary data?

def existing_diary():
    import pandas as pd
    existing_name = input("Access your diary by entering the diary name: ")
    df = pd.read_csv(existing_name + '.csv')
    df.to_csv(existing_name + '.csv', mode='a')
    print("Today's meals have been saved.")
    
def new_diary():
    import pandas as pd
    new_name = input("Create a new diary. Please enter a diary name in lower case: ")
    df = pd.DataFrame (dict)
    try:
        df.to_csv(new_name + '.csv', mode="x")
        df = pd.read_csv(new_name + '.csv')
        df.to_csv(new_name + '.csv', mode='a')
    except FileExistsError:
        print("This diary name already exists. Please enter a new diary name when prompted.")
        new_diary()

diary_options()
diary_selections()
existing_diary()
new_diary()
