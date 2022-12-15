# Upon executing the program users are prompted to enter today's meals.

from termcolor import colored
print(colored("Welcome to your food diary! Easily track your meals each day.", 'blue'))
#add some other instructions. i.e. follow the prompts and features.
print(colored("Enter today's meals - breakfast, lunch, dinner and snack - when prompted.", 'blue'))

# Function to call today's date
def today_date():
    from datetime import date
    date_today = date.today()
    return date_today.strftime('%d-%m-%y')

# Function for user to input meals. If there is a blank entry, users will see the prompt until they input the meal. Meals are then saved to a dictonary.
def meal_input():
    breakast_input = ''
    while True:
        breakfast_input = input("Enter breakfast: ")
        if breakfast_input:
            break
    lunch_input = ''
    while True:
        lunch_input = input("Enter lunch: ")
        if lunch_input:
            break
    dinner_input = ''
    while True:
        dinner_input = input("Enter dinner: ")
        if dinner_input:
            break
    snack_input = ''
    while True:
        snack_input = input("Enter snack: ")
        if snack_input:
            break
    date_input = today_date
        #need error handling for input that is not a string or word, only numbers.
    breakfast_list = [breakfast_input]
    lunch_list = [lunch_input]
    dinner_list = [dinner_input]
    snack_list = [snack_input]
    date_list = [date_input()]
    meals_dict = {'date': date_list, 'breakfast': breakfast_list, 'lunch': lunch_list, 'dinner': dinner_list, 'snack': snack_list}
    print(meals_dict)
    return meals_dict

def add_input(meals_dict):
    from termcolor import colored
    import pandas as pd
    df = pd.DataFrame (meals_dict)
    try:
        df.to_csv('diary.csv', index=False, header=True, mode="x")
    except FileExistsError:
        df.to_csv('diary.csv', index=False, header=False, mode="a")
    print(colored("Today's meals have been saved.", 'green'))
    return df

def additional_options():
    from termcolor import colored
    print(colored("Here are some additional diary features. When prompted, enter the number corresponding to your selection: ", 'blue'))
    from prettytable import PrettyTable
    options_table = PrettyTable (["Number", "Feature"])
    options_table.add_row(["1", "Edit today's meals"])
    options_table.add_row(["2", "View diary"])
    options_table.add_row(["3", "Exit session"])
    print(options_table)

def additional_selections():
    from termcolor import colored
    selection_input = input("Enter your selection: ")
    if selection_input == "1":
        edit_diary()
    elif selection_input == "2":
        view_diary()
    elif selection_input == "3":
        print(colored("Thanks for using the food diary. Come back tomorrow to input and track your meals.", 'blue'))
        quit()
    else:
        print(colored("Your selection isn't recognised. Please try again.", 'red'))
        additional_options()
        additional_selections()

def edit_diary():
    import pandas as pd
    from termcolor import colored
    edit_today = input("Enter meal to edit: ")
    if edit_today == "breakfast":
        edit_breakfast = input("Enter new breakfast: ")
        df = pd.read_csv('diary.csv', index_col='date')
        df.loc[today_date(), 'breakfast'] = edit_breakfast
        df.to_csv('diary.csv')
        print(colored("Today's breakfast has been edited.", 'green'))
        additional_options()
        additional_selections()
    elif edit_today == "lunch":
        edit_lunch = input("Enter new lunch: ")
        df = pd.read_csv('diary.csv', index_col='date')
        df.loc[today_date(), 'lunch'] = edit_lunch
        df.to_csv('diary.csv')
        print(colored("Today's lunch has been edited.", 'green'))
        additional_options()
        additional_selections()
    elif edit_today == "dinner":
        edit_dinner = input("Enter new dinner: ")
        df = pd.read_csv('diary.csv', index_col='date')
        df.loc[today_date(), 'dinner'] = edit_dinner
        df.to_csv('diary.csv')
        print(colored("Today's dinner has been edited.", 'green'))
        additional_options()
        additional_selections()
    elif edit_today == "snack":
        edit_snack = input("Enter new snack: ")
        df = pd.read_csv('diary.csv', index_col='date')
        df.loc[today_date(), 'snack'] = edit_snack
        df.to_csv('diary.csv')
        print(colored("Today's snack has been edited.", 'green'))
        additional_options()
        additional_selections()
    else:
        print(colored("Your input isn't recognised. Please try again.", 'red'))
        edit_diary()

def view_diary():
    print(colored("Here's your food diary.", 'blue'))
    from prettytable import PrettyTable
    table_view = PrettyTable()
    from prettytable import from_csv
    fp = open("diary.csv", "r")
    table_view = from_csv(fp)
    print(table_view)
    additional_options()
    additional_selections()

today_date()
meals_dict = meal_input()
add_input(meals_dict)
additional_options()
additional_selections()
edit_diary()
view_diary()