#!/bin/bash

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

# Check if requirements.txt exists
if [ ! -f requirements.txt ]; then
    echo "requirements.txt not found. Please create a requirements.txt file and try again."
    exit 1
fi

# Install requirements from requirements.txt
while read -r package; do
    pip3 show "$package" >/dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "Installing $package..."
        pip3 install "$package"
    else
        echo "$package is already installed."
    fi
done < requirements.txt

# Run DateTimeChecker.py
python3 "${0%/*}/main.py"
