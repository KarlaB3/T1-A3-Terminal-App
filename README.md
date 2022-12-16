# T1 A3 Food Diary Terminal App
The purpose of this terminal app is to allow users to track their daily meals. Users can input today's and yesterday's meals in the app and view their food diary in table format on the terminal screen.

Users also have the opportunity to edit today's meals in case they have made a mistake or omitted information.

*Note:* the app is designed to form a daily habit around tracking meals. Therefore, only today and yesterday's meals can be inputted. Users are unlikely to remember what they ate a week ago, let alone several days ago so it is unnecessary to include a function for entering and editing historic data past yesterday.

**PEP8** styling conventions were used to ensure readability and consistency in code. This includes:
* Indentation of 4 spaces per indentation level.
* Imports on separate lines.
* Avoiding extraneous whitespace in expressions and statements.
* Using full sentence comments that are clear and easily understandable.
* Function and variable names in lowercase, with words separated by underscores.

**GitHub Project Link**  
View the Github repo here: https://github.com/KarlaB3/T1-A3-Terminal-App

**Presentation Video**  
View the presentation video here: 

**Project Management Board**  
View the Trello project management board here: https://trello.com/b/TwGduS2x/t1a3-terminal-app

**Testing Process**  
View the manual test case procedures and results here: https://docs.google.com/spreadsheets/d/1VfLTricsIO6EEbugapw_jGdTI7tB39GkXV33-ZSg-Mg/edit?usp=sharing 

**Tech Stack:**
* Python source code, using the PEP8 styling convention written in Visual Studio Code.
* Python libraries: 
    * Pandas for creating dataframes and reading and writing to the .csv diary file. 
    * Datetime for calling today's and yesterday's date.
    * Prettytable for listing additional user options and to display the diary in table format in the terminal window.
    * Termcolor for coloured text to highlight important messages (green - confirmations, blue - instructions, red - errors).
* Markdown ReadMe file written in Visual Studio Code.
* GitHub for managing source code changes and tracking and controlling versions of the source code.
* Bash .sh file to execute the program.

# About The Project

## App Features
Three main features that make up the Food Diary terminal app are below.

**Input of Meals**  
This feature uses an intitial datetime function (today and yesterday) to check if users have inputted meals today and yesterday.

If there is no input for today and yesterday, the today and yesterday input functions prompt users to enter their meals - breakfast, lunch, dinner, snack. Input is saved as a dictionary to be called upon later, and displayed for the user to view immediately.

While loops are used to ensure users cannot enter an empty value - they must enter something for each meal for the program continue. For example, users must initially enter a value for breakfast before moving to lunch, then dinner. 

Implementation plan in Trello:  
![meal input feature Trello implementation plan](./docs/input-meals-feature.png)

**Reading and Writing to CSV**
This feature utilises Pandas to convert the meal dictionary into a DataFrame that is then saved as a .csv file. 

When a user first executes the program, 

Implementation plan in Trello:  
![csv read and write feature Trello implementation plan](./docs/csv-read-write-feature.png)


**Editing Meals**



## Implementation Plan
The project plan was tracked using Trello: https://trello.com/b/TwGduS2x/t1a3-terminal-app 

The project was broken down into 5 stages:
1. Initial Planning.   - screenshot and explanation
2. Planning Progress - screenshot & explanation


## Testing
Manual testing was used to test two functions critical to ensuring the program is ran as expected and improve the overall user experience. The two features tested were 


What was your process?
what were the results?
Link to the spreadsheet in docs folder. but also link to Google Spreadsheets. https://docs.google.com/spreadsheets/d/1VfLTricsIO6EEbugapw_jGdTI7tB39GkXV33-ZSg-Mg/edit?usp=sharing  

# Help Documentation
Design help documentation which includes a set of instructions which accurately describe how to use and install the application.

You must include:
- steps to install the application
- any dependencies required by the application to operate
- any system/hardware requirements
- how to use any command line arguments made for the application navigate to src folder in the zip file in CLI 'bash run_app.sh'