# !/bin/bash

# Check the correct version of Python is installed.
if command -v python3 &>/dev/null; 
then
    # Create a virtual environment
    python3 -m venv venv
    # Activate the virtual environment
    source venv/bin/activate
    # Install all Python packages required for running the food diary program
    pip install -r requirements.txt
    # Run the food diary program
    python3 food_diary.py
else
  # Display an error message stating Python needs to be installed with instructions.
  echo "Error: This program requires Python 3 to be installed. Visit https://www.python.org/downloads/ to download and install."
fi
exit
