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
        print(f"Current Balance:${self.__account_balance:.2f}")
