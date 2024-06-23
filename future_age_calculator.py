# Ask the user to input their current age
current_age = int(input("How old are you? "))

# Calculate the user's age in 2050
current_year = 2023
future_year = 2050
years_until_future = future_year - current_year
future_age = current_age + years_until_future

# Result is the user's age in 2050
print (f"In 2050, you will be {future_age} years old.")