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
    echo "$REQUIREMENTS_FILE not found. Please create a requirements.txt file and try again."
    exit 1
fi

# Install requirements from requirements.txt
while read -r req; do
    # Use awk to split the string into package name and version
    package=$(echo "$req" | awk -F'==' '{print $1}')
    version=$(echo "$req" | awk -F'==' '{print $2}')
    # Remove leading and trailing spaces from the version
    version=$(echo "$version" | awk '{gsub(/^[ \t]+|[ \t]+$/, ""); print}')

    package_info=$(pip3 show "$package")
    if echo "$package_info" | grep -q "Version: $version" ; then
        echo "${package} is already installed."
    else
        echo "Installing ${package}..."
        pip3 install "${package}"
    fi
done < "$REQUIREMENTS_FILE"


# Run Tests
python3 -m unittest discover
read -p "Press enter to exit..." continue