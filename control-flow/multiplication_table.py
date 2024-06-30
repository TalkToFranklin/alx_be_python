# Ask the user to enter a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table
for i in range(1, 10):
    product = number * i
    print(f"{number} * {i} = {number * i}")

# To check the range of the for loop
for i in range(1, 10):
    print(f"Iteration {i}")