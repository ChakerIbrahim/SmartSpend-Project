from user import User

first_user = User("jalil.w@gmail.com","Jalil")
second_user = User("Aballah_A@outlook.com","Abdallah")

first_user.make_deposit(500).make_withdraw(200).display_user_balance()
second_user.make_deposit(500).display_user_balance()