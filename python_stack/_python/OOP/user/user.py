class User:
    def __init__(self,email,name):
        self.email= email
        self.name = name
        self.balance = 0
    
    def make_deposit(self,amount):
        self.balance += amount
        return self
    
    def make_withdraw(self,amount):
        self.balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"User:{self.name} Balance:{self.balance}")
        
    def transfer_money(self,other_user,amount):
        self.balance -= amount
        other_user.balance += amount
        return self
# Create 3 users
first_user = User("jalil.w@gmail.com","Jalil")
second_user = User("Aballah_A@outlook.com","Abdallah")
third_user = User("Husni_ma2ati@yahoo.com","Husni")
# First user: 3 deposits and 1 withdrawal
# Second user: 2 deposits and 2 withdrawals
# Third user: 1 deposit and 3 withdrawals
first_user.make_deposit(1000).make_deposit(1000).make_deposit(3000).make_withdraw(500)
second_user.make_deposit(1500).make_deposit(500).make_withdraw(200).make_withdraw(50)
third_user.make_deposit(200).make_withdraw(50).make_withdraw(50).make_withdraw(100)

first_user.display_user_balance()
second_user.display_user_balance()
third_user.display_user_balance()

# BONUS: transfer money
first_user.transfer_money(third_user,500)

first_user.display_user_balance()
second_user.display_user_balance()
third_user.display_user_balance()
