import csv
from datetime import datetime

# Define the file path relative to the main execution file
FILE_PATH = 'data/wellness_logs.csv'
HEADERS = ['Date', 'SleepHours', 'WaterLiters', 'ExerciseMinutes']

def load_logs():
    """
    Reads the entire history of wellness logs from the CSV file.
    Handles file not found by creating a new, empty file (Error Handling).
    Returns a list of dictionaries (one dictionary per log entry).
    """
    try:
        with open(FILE_PATH, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        # Create the file and write headers if it doesn't exist
        print(f"INFO: Data file not found. Creating a new file at {FILE_PATH}")
        with open(FILE_PATH, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=HEADERS)
            writer.writeheader()
        return []
    except Exception as e:
        print(f"ERROR: Could not load data due to an unexpected error: {e}")
        return []

def save_log(log_data):
    """
    Appends a new wellness log entry to the CSV file.
    log_data is a dictionary containing the new record.
    """
    # Use 'a' for append mode. newline='' prevents extra blank rows.
    try:
        with open(FILE_PATH, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=HEADERS)
            writer.writerow(log_data)
        return True
    except Exception as e:
        print(f"ERROR: Could not save data: {e}")
        return False

def show_history(logs):
    """
    Displays all logs in a formatted table.
    """
    if not logs:
        print("\n--- No logs found in history. Start logging today! ---")
        return

    print("\n--- Full Wellness History ---")
    # Print header
    print(f"{'Date':<12} | {'Sleep (hrs)':<12} | {'Water (L)':<10} | {'Exercise (min)':<14}")
    print("-" * 52)
    
    # Print data
    for log in logs:
        # Data structure concept: accessing values by key
        print(f"{log['Date']:<12} | {log['SleepHours']:<12} | {log['WaterLiters']:<10} | {log['ExerciseMinutes']:<14}")
    print("-" * 52)
