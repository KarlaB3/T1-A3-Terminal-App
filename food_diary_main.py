#Upon executing the program users are prompted to enter their meals.
print("Welcome to the food diary program where you can easily track your meals each day.")

def today_date():
    from datetime import date
    today_date = date.today()
    print(today_date)

def meal_input():
    print("Enter today's meals when prompted.")
    breakfast_input = input("Enter breakfast: ")
    lunch_input = input("Enter lunch: ")
    dinner_input = input("Enter dinner: ")
    snack_input = input("Enter snack: ")
        #need error handling for input that is not a string or word, only numbers.
        #for loop?

    import pandas as pd
    breakfast_list = [breakfast_input]
    lunch_list =[lunch_input]
    dinner_list = [dinner_input]
    snack_list = [snack_input]
    meals_dict = {'breakfast': breakfast_list, 'lunch': lunch_list, 'dinner': dinner_list, 'snack': snack_list}
    #add today's date to dictionary
    df = pd.DataFrame (meals_dict)
    try:
        df.to_csv('diary.csv', mode="x")
    except FileExistsError:
        df.to_csv('diary.csv', mode="a")

    meals_output = f'Your meals for today are: {breakfast_input, lunch_input, dinner_input, snack_input}'
    print(meals_output)
    print(meals_dict)

    meals_dict = meal_input()

meal_input()

def view_diary():
    print(meals_output)

#how to call the dictionary again in another function as I need to create functions that do this:
# #edit input
#view diary
#download diary
