# Simple CLI Human Wellness Tracker

## Overview of the Project
The Simple CLI Human Wellness Tracker is a text-based application designed to help users log and analyze their daily health habits. Built using **Python**, it tracks three core metrics: **Sleep (hours), Water Intake (liters), and Exercise (minutes)**. This project demonstrates the application of core programming concepts such as modularity, file handling, basic data structures (lists/dictionaries), and error handling.

## Features
The tracker includes three major functional modules:
1. Daily Log Entry (Data Input & Processing): Allows the user to record wellness metrics for a specific date, with data persistence handled via a local CSV file. 
2. View History (Clear Input/Output): Reads and displays all recorded logs in a clear, easy-to-read table format. 
3. Weekly Summary (Reporting or Analytics): Calculates and displays the average sleep, water, and exercise for the last seven days to provide quick trend analysis. 

## Technologies/Tools Used
Programming Language: Python 3.x
Data Storage: Local CSV File (wellness_logs.csv)
Version Control: Git & GitHub 

## Steps to Install & Run the Project
This project is built using standard Python libraries, so no additional dependencies are required.

1.  Clone the Repository:
    Use Git to download the project files:
    ```bash
    git clone [Your GitHub Repository URL]
    cd Human-Wellness-Tracker
    ```
2.  Verify Python Installation:
    Ensure Python 3 is installed on your system. You can check the version using:
    ```bash
    python --version 
    # OR 
    python3 --version
    ```
3.  Run the Application:
    Execute the main file (main.py) from the root directory:
    ```bash
    python main.py
    # OR
    python3 main.py
    ```

## Instructions for Testing
The primary testing approach is manual validation.

Functionality Test: Select the daily log option. Enter sample numeric data. Select the view history option to verify the new log has been saved and is displayed correctly.
Error Handling Test: When prompted for a numeric input (like sleep hours), intentionally enter text (e.g., "seven"). The program should display an error message and prompt you to re-enter the input correctly. 
