from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.__is_borrowed = False
        self.__borrower = None
        self.__due_date = None

    def borrow(self, user, due_date):
        if self.__is_borrowed:
            print(f"{self.title} is already borrowed.")
        else:
            self.__is_borrowed = True
            self.__borrower = user
            self.__due_date = due_date
            print(f"{user} borrowed {self.title}. Due date: {due_date}")

    def return_item(self):
        if self.__is_borrowed:
            print(f"{self.title} returned by {self.__borrower}.")
            self.__is_borrowed = False
            self.__borrower = None
            self.__due_date = None
        else:
            print(f"{self.title} was not borrowed.")

    def check_availability(self):
        return not self.__is_borrowed

    def notify_overdue(self, days_late):
        if days_late > 0 and self.__is_borrowed:
            fee = self.calculate_late_fee(days_late)
            print(f"Notification: {self.__borrower}, {self.title} is overdue.")
            print(f"Days late: {days_late}")
            print(f"Late fee: ${fee}")

    @abstractmethod
    def calculate_late_fee(self, days_late):
        pass


class Book(LibraryItem):
    def calculate_late_fee(self, days_late):
        return days_late * 1


class Magazine(LibraryItem):
    def calculate_late_fee(self, days_late):
        return days_late * 0.5


class DVD(LibraryItem):
    def calculate_late_fee(self, days_late):
        return days_late * 2


# Testing the system

book1 = Book("Python Basics", 101)
magazine1 = Magazine("Tech Monthly", 201)
dvd1 = DVD("OOP Tutorial", 301)

book1.borrow("Jalil", "2026-05-20")
print(book1.check_availability())

book1.notify_overdue(3)

book1.return_item()
print(book1.check_availability())

print()

magazine1.borrow("Ahmad", "2026-05-18")
magazine1.notify_overdue(4)

print()

dvd1.borrow("Sara", "2026-05-15")
dvd1.notify_overdue(2)