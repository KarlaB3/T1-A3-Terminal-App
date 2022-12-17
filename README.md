# T1 A3 Food Diary Terminal App
The purpose of the Food Diary terminal app is to allow users to track their daily meals.

The app is targeted for users who want to form a daily habit around recording their meals, and ensuring they stay on track with their food and nutrition goals.

Users can input today's and yesterday's meals in the app and view their food diary in table format on the terminal screen. Users also have the opportunity to edit today's meals in case they have made a mistake or omitted information.

*Note:* the app is designed to help users form a daily habit around recording meals. Therefore, only today and yesterday's meals can be inputted and edited. Users are unlikely to remember what they ate a week ago, let alone several days ago so it is unnecessary to include a function for entering and editing historic data past yesterday.

**PEP8** styling conventions were used to ensure readability and consistency in code. This includes:
* Indentation of 4 spaces per indentation level.
* Imports on separate lines.
* Avoiding extraneous whitespace in expressions and statements.
* Using full sentence comments that are clear and easily understandable.
* Function and variable names in lowercase, with words separated by underscores.

**GitHub Project Link**  
View the Github repo here: https://github.com/KarlaB3/T1-A3-Terminal-App

**Presentation Video**  
View the presentation video here: https://vimeo.com/782205831/1e393d3ebc

**Project Management Board**  
View the Trello project management board here: https://trello.com/b/TwGduS2x/t1a3-terminal-app

**Testing**  
View the manual test case scenarios and results in Google Docs: https://docs.google.com/spreadsheets/d/1VfLTricsIO6EEbugapw_jGdTI7tB39GkXV33-ZSg-Mg/edit?usp=sharing

**Tech Stack:**
* Python source code, using the PEP8 styling convention written in Visual Studio Code.
* Python libraries: 
    * Pandas for creating dataframes and reading and writing to the .csv diary file. 
    * Datetime for calling and returning today's and yesterday's date.
    * Prettytable for listing additional user options and to display the diary in table format in the terminal window.
    * Termcolor for coloured text to highlight important messages (green - confirmations, blue - instructions, red - errors).
* Markdown ReadMe file written in Visual Studio Code.
* GitHub for managing source code changes and tracking and controlling versions of the source code.
* Bash .sh script to execute the program.

# About The Project

## App Features
Three main features that make up the Food Diary terminal app are below.

**Input of Meals**  
This feature uses an intitial datetime function (today and yesterday) to check if users have inputted meals today and yesterday.

If there is no input for today and yesterday, the today and yesterday input functions prompt users to enter their meals - breakfast, lunch, dinner, snack. Input is saved as a dictionary to be called upon later, and displayed for the user to view immediately.

While loops are used to ensure users cannot enter an empty value - they must enter something for each meal for the program continue. For example, users must initially enter a value for breakfast before moving to lunch, then dinner. 

Confirmations are displayed to the user when they have successfully inputted their meals.

Feature implementation plan in Trello:  
![meal input feature Trello implementation plan](./docs/input-meals-feature.png)

**Reading and Writing to CSV**  
This feature utilises Pandas to convert the meal dictionary into a DataFrame which is then saved as a .csv file. 

When a user first runs the app, the add input function checks if a .csv file already exists. This ensures that meal data is not duplicated across multiple files, so the diary is stored in one place for easy viewing and editing. 

If a diary .csv file does not exist, it is created and referenced later for reading and writing when inputting and editing meals. If a diary .csv file already exists, it is opened in 'append' mode and meals data is appended to the next blank row.

A try except statement is used to handle the exception in this case. to check if the diary.csv file already exists. 

Feature implementation plan in Trello:  
![csv read and write feature Trello implementation plan](./docs/csv-read-write-feature.png)

**Editing Meals**  
This feature utilises a today datetime function and Pandas to locate the row containing today's meals and then overwrite existing meal data in that row with what users have inputted.

Users are given the option to edit a specific meal type - breakfast, lunch, dinner or snack. They must enter the correctly formatted value, otherwise they receive an error message that the input isn't recognised, and to try again. If else statements are used to handle the input errors in this case. Users are then prompted to enter the meal type of choice to edit.

Once meals are edited, users are prompted to view additional diary features including viewing the diary or exiting the program.

Feature implementation plan in Trello:  
![edit meals feature Trello implementation plan](./docs/editing-meals-feature.png)

## Implementation Plan
The project plan was tracked using Trello. View the board here: https://trello.com/b/TwGduS2x/t1a3-terminal-app 

The project was broken down into 5 stages:

**1. Initial Planning**  
In the initial planning stage a full outline of the tasks and sub-tasks required to complete the project were listed in Trello in order of what was to be actioned and completed first. This ensured no steps were missed and provided a useful guideline for the order of operations.

![project plan stage 1](./docs/stage-1-initial-plan.png)

**2. Planning Progress**  
The first step, which was the initial approval of the app idea by Coder Academy educators, was critical to moving onto the rest of the project. Upon approval, a full app plan was developed including target users and app features. Then decisions on key app features and functionality were made, and the research of Python packages and useful functions commenced.

![project plan stage 2](./docs/stage-2-planning-progress.png)

**3. Testing & Development**  
The testing and development stage took the majority of project time. Manual tests were conducted on two key features (to be discussed later in this document) and then developed in Visual Studio Code. Key feature plans were also created as these features are critical to the app running as expected, without errors. 

![project plan stage 3](./docs/stage-3-testing-development.png)

**4. Scripting & Documentation**  
In this stage a bash script was written to facilitate execution of the program. In addition, documentation (README.md) was written containing all information necessary for users to run the program plus additional helpful information about the program and its functions and features.

![project plan stage 4](./docs/stage-4-scripting-documentation.png) 

**5. Completion & Submission**  
The fifth and final stage was to package up all files and documentation into a .zip file as per the assessment requirements, and submit via Canvas.

![project plan stage 5](./docs/stage-5-completion.png) 

## Testing
Prior to development manual testing was used to test two functions critical to ensuring the app runs as expected, and to improve the overall user experience. 

Testing was documented in Google Sheets: https://docs.google.com/spreadsheets/d/1VfLTricsIO6EEbugapw_jGdTI7tB39GkXV33-ZSg-Mg/edit?usp=sharing 

**Test Case: Meal input**   
**Test Case:** Testing of today and yesterday meal input functions.  
**Requirements:** Users are prompted to enter their meals for the day. If they have missed yesterday's input, they are prompted to enter yesterday's meals. Meals are then displayed on the screen with a confirmation message.  
  	**Test type:** Unit test to ensure the meal input functions work as intended and captures and displays meal input and a confirmation message on the terminal screen.

Three scenarios were tested:
* *First time use*: where the user has never used the app before, they're prompted to enter today's meals in order of breakfast, lunch, dinner and snack, and the expected result is to display their inputted meals on the screen along with a confirmation message advising their input has been saved. The test failed where users did not input a meal, producing a blank value. The solution was to use a while loop to ensure meals are inputted before moving onto the next step.
* *User has inputted yesterday's meals, but not today's meals*: users are prompted today's meals in order of breakfast, lunch, dinner and snack, and the expected result is to display their inputted meals on the screen along with a confirmation message advising their input has been saved. The test failed where users did not input a meal, producing a blank value. The solution was to use a while loop to ensure meals are inputted before moving onto the next step. 
* *User has inputted today's meals, but not yesterday's meals*: once the user has inputted today's meals, the app checks that there is existing data for yesterday's meals. If there is no data for yesterday, users are prompted to enter yesterday's meals in order of breakfast, lunch, dinner and snack, and the expected result is to display their inputted meals on the screen along with a confirmation message advising their input has been saved. The test failed where users did not input a meal, producing a blank value. The solution was to use a while loop to ensure meals are inputted before moving onto the next step. 

**Test Case: Save meals to .csv file**   
**Test Case:** Testing of function to write meals to .csv file.  
**Requirements:** Meals are inputted then saved as a meals dictionary. The meals dictionary is converted to a Pandas dataframe and saved as a .csv file ('diary.csv').  
**Test type:** Unit test to ensure the function works as intended and saves meal input into a diary.csv file.

Two scenarios were tested:
* *First time use*: where the user has never used the app before, they're prompted to enter today's meals. Input is saved as a dictionary, then converted to a Pandas dataframe and saved as a .csv file ('diary.csv'). During first time use, the app creates the diary.csv and sets the columns: date, breakfast, lunch, dinner, snack.
* *User has previously inputted meals*: Users are prompted to enter today's and/or yesterday's meals. Input is saved as a dictionary, then converted to a Pandas dataframe and saved as a .csv file ('diary.csv'). A FileExistsError initially occurred because the app did not check if a .csv file already existed. The solution was to use a try except statement to check if the file already exists. If hte file exists, it is opened in 'append' mode and meals data appended to the next blank row.

# Help Documentation
Dependencies:
* Bash command line interface (CLI) shell program.
* Python 3.

Follow these instructions to successfully install and run the app:
1. Download the .zip file titled 'KarlaBucoy-T1A3.zip'.
2. Unzip 'KarlaBucoy-T1A3.zip'. 
2. Open your Bash CLI shell terminal.
3. Navigate to where the 'KarlaBucoy-T1A3' unzipped directory is located using the 'cd' command.
4. Navgiate to the the 'src' directory using the 'cd' command.
4. Run the 'run_app.sh' script using 'bash run_app.sh' command.

The run_app script does the following:
* Checks if you have the correct version of Python installed. If not, an error message will be displayed providing a link to download and install Python 3.
* Creates a virtual environment.
* Activates a virtual environment.
* Installs the required Python packages via the 'requirements.txt' file.
* Runs the 'food_diary.py' program.