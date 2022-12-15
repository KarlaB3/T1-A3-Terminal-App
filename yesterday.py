def yesterday_check():
    import pandas as pd
    check_date = df.isin([yesterday_date]).any().any()
    while check_date is True:
        additional_options()
        additional_selections()
    else:
        yesterday_meal_input()
        add_input(meals_dict)

# Function to call yesterday's date
def yesterday_date():
    from datetime import date
    from datetime import timedelta
    date_today = date.today()
    date_yesterday = date_today - timedelta(days = 1)
    return date_yesterday.strftime('%d-%m-%y')

# User to input meals. If there is a blank entry, users will see the prompt until they input the meal. Meals are then saved to a dictonary.
def yesterday_meal_input():
    yesterday_breakast_input = ''
    while True:
        yesterday_breakfast_input = input("Enter breakfast: ")
        if yesterday_breakfast_input:
            break
    yesterday_lunch_input = ''
    while True:
        yesterday_lunch_input = input("Enter lunch: ")
        if yesterday_lunch_input:
            break
    yesterday_dinner_input = ''
    while True:
        yesterday_dinner_input = input("Enter dinner: ")
        if yesterday_dinner_input:
            break
    yesterday_snack_input = ''
    while True:
        yesterday_snack_input = input("Enter snack: ")
        if yesterday_snack_input:
            break
    yesterday_input = yesterday_date
        # need error handling for input that is not a string or word, only numbers.
    yesterday_breakfast_list = [breakfast_input]
    yesterday_lunch_list = [lunch_input]
    yesterday_dinner_list = [dinner_input]
    yesterday_snack_list = [snack_input]
    yesterday_date_list = [yesterday_input()]
    yesterday_meals_dict = {'date': yesterday_date_list, 'breakfast': yesterday_breakfast_list, 'lunch': yesterday_lunch_list, 'dinner': yesterday_dinner_list, 'snack': yesterday_snack_list}
    print(yesterday_meals_dict) # don't forget to remove this
    return yesterday_meals_dict

# Save the meals dictionary into a .csv file
def add_yesterday_input(yesterday_meals_dict):
    from termcolor import colored
    import pandas as pd
    df = pd.DataFrame (yesterday_meals_dict)
    try:
        df.to_csv('diary.csv', index=False, header=True, mode="x")
    except FileExistsError:
        df.to_csv('diary.csv', index=False, header=False, mode="a")
    print(colored("Yesterday's meals have been saved.", 'green'))
    return df

yesterday_check()
yesterday_date()
meals_dict = yesterday_meal_input()
add_input(meals_dict)



