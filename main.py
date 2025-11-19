import data_handler
import analytics
from datetime import datetime

def display_menu():
    """
    Shows the main menu to the user.
    """
    print("\n==================================")
    print("  SIMPLE CLI HUMAN WELLNESS TRACKER")
    print("==================================")
    print("1. Log Daily Data")
    print("2. View History")
    print("3. View Weekly Summary")
    print("4. Exit")
    print("----------------------------------")

def get_daily_input():
    """
    Handles user input for daily logging and ensures data validation (Error Handling).
    """
    today_date = datetime.now().strftime('%Y-%m-%d')
    print(f"\n--- Logging Data for: {today_date} ---")
    
    # Input validation loop
    while True:
        try:
            sleep = float(input("Enter Sleep Hours (e.g., 7.5): "))
            water = float(input("Enter Water Intake (Liters, e.g., 2.0): "))
            exercise = float(input("Enter Exercise Minutes (e.g., 45): "))
            
            if sleep < 0 or water < 0 or exercise < 0:
                print("Input cannot be negative. Please re-enter.")
                continue

            break # Exit loop if all inputs are valid numbers

        except ValueError:
            # Reliability Requirement: Handles non-numeric input gracefully
            print("Invalid input. Please enter a valid number (e.g., 7.5, not 'seven').")

    log_data = {
        'Date': today_date,
        'SleepHours': f"{sleep:.1f}",
        'WaterLiters': f"{water:.1f}",
        'ExerciseMinutes': f"{int(exercise)}",
    }

    if data_handler.save_log(log_data):
        print(f"\nSUCCESS: Log for {today_date} saved.")

def main():
    """
    The main execution loop of the program.
    """
    while True:
        display_menu()
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            get_daily_input()
        
        elif choice == '2':
            logs = data_handler.load_logs()
            data_handler.show_history(logs)
            
        elif choice == '3':
            logs = data_handler.load_logs()
            analytics.calculate_weekly_summary(logs)
            
        elif choice == '4':
            print("\nThank you for using the Wellness Tracker. Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    # Ensure the data folder exists before starting the application
    import os
    if not os.path.exists('data'):
        os.makedirs('data')
        
    main()
