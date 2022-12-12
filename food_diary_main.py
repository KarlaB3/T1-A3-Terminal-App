#Upon executing the program users are prompted to enter their meals.
print("Welcome to your food diary! Easily track your meals each day.")
#add some other instructions. i.e. follow the prompts and features.
print("Enter today's meals - breakfast, lunch, dinner and snack - when prompted.")

def today_date():
    from datetime import date
    date_today = date.today()
    return date_today.strftime('%d-%m-%y')

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
    import pandas as pd
    df = pd.DataFrame (meals_dict)
    try:
        df.to_csv('diary.csv', index=False, header=True, mode="x")
    except FileExistsError:
        df.to_csv('diary.csv', index=False, header=False, mode="a")
    print("Today's meals have been saved.")
    return df

def additional_options():
    print("Here are some additional diary features. When prompted, enter the number corresponding to your selection: ")
    from prettytable import PrettyTable
    options_table = PrettyTable (["Number", "Feature"])
    options_table.add_row(["1", "Edit today's meals"])
    options_table.add_row(["2", "View diary"])
    options_table.add_row(["3", "Exit session"])
    print(options_table)

def additional_selections():
    selection_input = input("Enter your selection: ")
    if selection_input == "1":
        edit_diary()
    elif selection_input == "2":
        view_diary()
    elif selection_input == "3":
        print("Thanks for using the food diary. Come back tomorrow to input and track your meals.")
        quit()
    else:
        print("Your selection isn't recognised. Please try again.")
        additional_options()
        additional_selections()

def edit_diary():
    import pandas as pd
    edit_today = input("Enter meal to edit: ")
    if edit_today == "breakfast":
        edit_breakfast = input("Enter new breakfast: ")
        df = pd.read_csv('diary.csv', index_col='date')
        df.loc[today_date(), 'breakfast'] = edit_breakfast
        df.to_csv('diary.csv')
        print("Today's breakfast has been edited.")
        additional_options()
        additional_selections()
    elif edit_today == "lunch":
        edit_lunch = input("Enter new lunch: ")
        df = pd.read_csv('diary.csv', index_col='date')
        df.loc[today_date(), 'lunch'] = edit_lunch
        df.to_csv('diary.csv')
        print("Today's lunch has been edited.")
        additional_options()
        additional_selections()
    elif edit_today == "dinner":
        edit_dinner = input("Enter new dinner: ")
        df = pd.read_csv('diary.csv', index_col='date')
        df.loc[today_date(), 'dinner'] = edit_dinner
        df.to_csv('diary.csv')
        print("Today's dinner has been edited.")
        additional_options()
        additional_selections()
    elif edit_today == "snack":
        edit_snack = input("Enter new snack: ")
        df = pd.read_csv('diary.csv', index_col='date')
        df.loc[today_date(), 'snack'] = edit_snack
        df.to_csv('diary.csv')
        print("Today's snack has been edited.")
        additional_options()
        additional_selections()
    else:
        print("Your input isn't recognised. Please try again.")
        edit_diary()

def view_diary():
    print("Here's your food diary.")
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