# Ask the user for the task
task = input("Enter your task: ")

# Ask the user for the task priority
priority = input("Priority (high/medium/low): ")

# Ask the user if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Consider completing it soon.")
    case "medium":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires attention today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Complete it when you have time.")
    case "low":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a low priority task, but it is time-bound. Try to complete it today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")