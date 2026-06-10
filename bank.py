from datetime import datetime

today = datetime.today()
print(today)

class BankAccount:
    def __init__(self, account_number, balance=0, owner_name, date_opened=today):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened
    
    def deposit (self,amount):
        self.amount +=amount
        print()
account1 = BankAccount("Acc101",100,"Ruth",)
