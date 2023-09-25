#!/bin/bash

# Check if Python3 is installed
if ! command -v python3 > /dev/null 2>&1; then
    echo "Python3 is not installed. Please install Python3 and try again."
    exit 1
fi

# Check if pip3 is installed
if ! command -v pip3 > /dev/null 2>&1; then
    echo "pip3 is not installed. Please install pip3 and try again."
    exit 1
fi

REQUIREMENTS_FILE="requirements.txt"
# Check if requirements.txt exists
if [ ! -f "$REQUIREMENTS_FILE" ]; then
    echo "$REQUIREMENTS_FILE not found. Please create a $REQUIREMENTS_FILE file and try again."
    exit 1
fi

# Install requirements from requirements.txt
pip3 install -r $REQUIREMENTS_FILE


# Run Tests
python3 -m unittest discover
read -p "Press enter to exit..." continue