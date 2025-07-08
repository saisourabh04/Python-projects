from User import User
from uuid import uuid4
from datetime import datetime

class Member(User):
    def __init__(self):
        super().__init__()
        self.member_id=str(uuid4())
        self.borrowed_books={}
        self.member_expiry=None
        self.register()

    def register(self):
        super().register()
        self.member_expiry=datetime.strptime(input('Enter a date: '),'%d-%m-%Y').date()

    def show_member(self):
        print(f"Member Details\nID:{self.member_id}\nName:{self.first_name} {self.last_name}\nEmail:{self.email}\nExpiry:{self.member_expiry}")

    def borrow_book(self,book):
        self.borrowed_books[book.isbn]=book
        print(f"You have borrowed the following {book.title} book ")

    def return_book(self,book_isbn):
        book= (
            self.borrowed_books.pop(book_isbn))
        print(f"You have returned the following {book.title} book ")

    def show_all_books(self):
        print("Members have the following books:")
        for book in self.borrowed_books:
            self.borrowed_books[book].show_book()







