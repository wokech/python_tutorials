class BankAccount:
    """Represents a bank account with balance and transaction history."""

    def __init__(self, owner, initial_balance):
        """Initialize a new bank account."""
        self.owner = owner
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        """Deposit money into the account."""
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        """Check the current balance of the account."""
        return self.balance

    def transaction_history(self):
        """View the transaction history of the account."""
        for transaction in self.transactions:
            print(transaction)

# Example usage
my_account = BankAccount("John Doe", 1000)
my_account.deposit(500)
my_account.withdraw(200)
print(f"Current balance: {my_account.check_balance()}")
my_account.transaction_history()