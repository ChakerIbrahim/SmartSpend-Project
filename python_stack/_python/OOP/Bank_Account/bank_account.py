class BankAccount:
    def __init__(self,name,int_rate,balance):
        self.name = name
        self.int_rate =int_rate
        self.balance = balance
# Deposit Money
    def deposit(self,amount):
        self.balance += amount
        return self
# Withdraw Money
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
# Display account info    
    def display_account_info(self):
        print(f"User:{self.name} Balance:${self.balance}")
        return self
 # Add interest       
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
# create 3 users  
first_account = BankAccount("Jalil",0.01,5000)
second_account = BankAccount("Abdallah",0.02,10000)
third_account = BankAccount("Husni",0.01,2)

# First account:
# 3 deposits, 1 withdrawal, yield interest, display info
first_account.deposit(1000).deposit(1000).deposit(1000).withdraw(500).yield_interest().display_account_info()
# Second account:
# 2 deposits, 4 withdrawals, yield interest, display info
second_account.deposit(2000).deposit(2000).withdraw(1000).withdraw(1500).withdraw(500).withdraw(200).yield_interest().display_account_info()
# Bonus to try the Insufficient funds
third_account.withdraw(5).yield_interest().display_account_info()

