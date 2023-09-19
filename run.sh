#!/bin/sh

# Check if Python is installed
python3 --version >/dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Python is not installed. Please install Python and try again."
    exit 1
fi

# Check if pip is installed
pip --version >/dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "pip is not installed. Please install pip and try again."
    exit 1
fi

# Check if requirements.txt exists
if [ ! -f requirements.txt ]; then
    echo "requirements.txt not found. Please create a requirements.txt file and try again."
    exit 1
fi

# Install requirements from requirements.txt
while read -r req; do
    pip show "$req" >/dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "Installing $req..."
        pip install "$req"
    else
        echo "$req is already installed."
    fi
done < requirements.txt

# Run DateTimeChecker.py
python3 "$(dirname "\$0")/main.py"
