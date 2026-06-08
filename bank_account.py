class BankAccount:

    def __init__(self, account_number, balance, owner_name, date_opened):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}")
        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

    def display_info(self):
        print("\n----- Account Information -----")
        print("Account Number:", self.account_number)
        print("Owner Name:", self.owner_name)
        print("Balance:", self.balance)
        print("Date Opened:", self.date_opened)

    def close_account(self):
        print(f"Account {self.account_number} has been closed.")

account1 = BankAccount(
    "ACC001",
    5000,
    "Ruth Ndiko",
    "2026-08-01"
)

account2 = BankAccount(
    "ACC002",
    10000,
    "Joseph Komba",
    "2026-08-05"
)



account1.display_info()
account1.deposit(2000)
account1.withdraw(1000)
account1.check_balance()
account1.close_account()


account2.display_info()
account2.deposit(5000)
account2.withdraw(3000)
account2.check_balance()
account2.close_account()