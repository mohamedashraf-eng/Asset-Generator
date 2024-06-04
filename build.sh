#!/bin/bash

rebuild=$1
ide=$2
num_cores=$(nproc)

# Color codes for styling
RED="\033[0;31m"
GREEN="\033[0;32m"
YELLOW="\033[0;33m"
BLUE="\033[0;34m"
BOLD="\033[1m"
RESET="\033[0m"

# Function to echo colored text
echo_color() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${RESET}"
}

# Function to check if a file exists
check_file_exists() {
    if [ ! -f "$1" ]; then
        echo_color $RED "${BOLD}Error: File '$1' not found.${RESET}"
        exit 1
    fi
}

# Pre conditions
echo "------------------------------------------------------------------------------------------------------"
echo_color $GREEN "${BOLD}Installing Dependencies${RESET}"

echo "------------------------------------------------------------------------------------------------------"

# Build the project
echo_color $GREEN "${BOLD}Generating project folder structure${RESET}"
python3 src/generate_full_project.py
echo_color $GREEN "${BOLD}Generating file template${RESET}"
python3 src/generator.py
