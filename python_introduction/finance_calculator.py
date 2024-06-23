# Ask the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Ask the user for their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

# Assume a simple annual interest rate of 5%
annual_interest_rate = 0.05

# Calculate the projected savings after one year, incorporating the interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * annual_interest_rate)

# Result
print (f"Your monthly savings are ${monthly_savings:.2f}.")
print (f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")