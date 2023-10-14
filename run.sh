#!/bin/bash

ENV_NAME=".venv"

if [ -d "$ENV_NAME" ]; then
    echo "Virtual environment '$ENV_NAME' already exists."
else
    echo "Creating virtual environment..."
    python3 -m venv $ENV_NAME
fi

source $ENV_NAME/bin/activate

# Check if Python is installed
python3 --version >/dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Python is not installed. Please install Python and try again."
    exit 1
fi

# Check if pip is installed
pip3 --version >/dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "pip is not installed. Please install pip and try again."
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


# Run main.py
python3 "${0%/*}/main.py"
