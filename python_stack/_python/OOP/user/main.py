class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self


user1 = User("Jalil")
user2 = User("Abdallah")
user3 = User("Husni")

user1.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(75).display_user_balance()

user2.make_deposit(300).make_deposit(100).make_withdrawal(50).make_withdrawal(25).display_user_balance()

user3.make_deposit(500).make_withdrawal(100).make_withdrawal(50).make_withdrawal(25).display_user_balance()

user1.transfer_money(user3, 100)

user1.display_user_balance()
user3.display_user_balance()