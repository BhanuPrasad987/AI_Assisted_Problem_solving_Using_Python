#Write a Python class named BankAccount with methods for deposit, withdraw, and check_balance,
# then analyze the generated code  and add comments explaining how each part of the class works.
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        # Initialize the BankAccount with account holder's name and an optional initial balance
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        # Method to deposit money into the account
        if amount > 0:
            self.balance += amount  # Increase balance by the deposit amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Method to withdraw money from the account
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount  # Decrease balance by the withdrawal amount
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        # Method to check the current balance of the account
        print(f"Current balance: ${self.balance:.2f}")