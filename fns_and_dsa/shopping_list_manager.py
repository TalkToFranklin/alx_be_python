# Create an empty shopping list using the \list function
shopping_list = []

# Function to display the menu
def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

# Function to add an item to the shopping list
def add_item():
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} added to the shopping list.")

# Function to remove an item from the shopping list
def remove_item():
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the shopping list.")
    else:
        print(f"{item} not found in the shopping list.")

# Function to display the current shopping list
def view_list():
    print("Current Shopping List:")
    for item in shopping_list:
        print("- " + item)

# Main loop
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        view_list()
    elif choice == "4":
        print("Exiting Shopping List Manager...")
        break
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()