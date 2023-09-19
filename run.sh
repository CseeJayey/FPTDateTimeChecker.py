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

REQUIREMENTS_FILE="requirements.txt"
# Check if requirements.txt exists
if [ ! -f "$REQUIREMENTS_FILE" ]; then
    echo "$REQUIREMENTS_FILE not found. Please create a $REQUIREMENTS_FILE file and try again."
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
        echo "${package}==${version} is already installed."
    else
        echo "Installing ${package}..."
        pip3 install "${package}"
    fi
done < "$REQUIREMENTS_FILE"


# Run main.py
python3 "${0%/*}/main.py"
