from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time in a readable format."""
    # Get the current date and time
    current_date = datetime.now()
    # Format the date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Print the formatted date and time
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    """Calculates the future date after adding a specified number of days to the current date."""
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    # Print the formatted future date
    print(f"Date after {days_to_add} days: {formatted_future_date}")

def main():
    """Main function to run the datetime exploration script."""
    # Display the current date and time
    current_date = display_current_datetime()
    
    # Prompt the user to enter the number of days to add
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # Calculate and display the future date
        calculate_future_date(current_date, days_to_add)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()