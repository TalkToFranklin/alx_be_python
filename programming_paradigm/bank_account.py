class BankAccount:
    """
    A class representing a simple bank account.
    
    Attributes:
        __account_balance (float): The current balance of the account.
    """
    def __init__(self, initial_balance=0):
        """
        Initializes a new instance of the BankAccount class.
        
        Args:
            initial_balance (float): The initial balance of the account. Defaults to 0.
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.
        
        Args:
            amount (float): The amount to be deposited.
        """
        self.__account_balance += amount

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if sufficient funds are available.
        
        Args:
            amount (float): The amount to be withdrawn.
        
        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Displays the current balance of the account in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")




# This program should always be in a separate file

import sys
from bank_account import BankAccount

def main():
    """
    The main function that serves as the entry point of the script.
    It interacts with the BankAccount class to perform banking operations.
    """
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
