from datetime import datetime, timedelta

def calculate_weekly_summary(logs):
    """
    Calculates the average sleep, water, and exercise for the last 7 days.
    Input logs are a list of dictionaries.
    """
    if not logs:
        print("ERROR: Cannot generate summary, no logs available.")
        return

    # Determine the date range (last 7 days including today)
    today = datetime.now().date()
    seven_days_ago = today - timedelta(days=7)
    
    recent_logs = []
    
    # Logic to filter logs to the last 7 days
    for log in logs:
        try:
            log_date = datetime.strptime(log['Date'], '%Y-%m-%d').date()
            if log_date > seven_days_ago and log_date <= today:
                recent_logs.append(log)
        except ValueError:
            # Simple Error Handling for badly formatted dates in the data file
            print(f"WARNING: Skipping log with invalid date format: {log['Date']}")
            continue

    if not recent_logs:
        print("--- No logs found in the last 7 days to generate a summary. ---")
        return

    total_sleep = 0.0
    total_water = 0.0
    total_exercise = 0.0
    count = len(recent_logs)

    # Calculate totals
    for log in recent_logs:
        try:
            # Data validation and conversion from string to float
            total_sleep += float(log['SleepHours'])
            total_water += float(log['WaterLiters'])
            total_exercise += float(log['ExerciseMinutes'])
        except ValueError:
            print("WARNING: Skipping log due to invalid numeric data.")
            count -= 1 # Adjust the count if a log is skipped

    if count == 0:
        print("--- No valid numeric logs found in the last 7 days. ---")
        return

    # Calculate Averages (Analytics)
    avg_sleep = total_sleep / count
    avg_water = total_water / count
    avg_exercise = total_exercise / count

    print("\n--- Last 7 Days Summary (Averages) ---")
    print(f"Days tracked: {count}")
    print(f"Average Sleep: {avg_sleep:.2f} hours")
    print(f"Average Water: {avg_water:.2f} liters")
    print(f"Average Exercise: {avg_exercise:.0f} minutes")
    print("-" * 40)
