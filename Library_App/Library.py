from Member import Member
from Book import Book



class Library():
    def __init__(self,name=None):
        self.name=name
        self.members={}
        self.books={}
        self.current_user=None
    def run(self):
        print(f"Welcome to Library {self.name}")
        choice=None
        while choice != 3:
            choice=int(input("""
            1.Member sign up
            2.Member sign in
            3.Member Exit
            Choose an option to proceed:
            """))
            if choice==1:
                member=Member()
                self.members[member.member_id]=member
                print("New member Info")
                member.show_member()
            elif choice==2:
                print("welcome to log in")
                member_id=input("enter member_id:")
                if member_id in self.members:
                    self.current_user=self.members[member_id]
                    self.current_user.login()
                    if self.current_user.logged_in:
                        self.member_portal()

    def member_portal(self):
        member_choice=None
        while member_choice!=4:
            member_choice=int(input("""
            Welcome to the member portal
             1.Borrow a book
             2.Return a book
             3.Show all books
             4.Exit
             Choose an option to proceed: """))
            if member_choice==1:
                self.show_books()
                isbn=input("enter isbn number to borrow: ")
                book=self.books[isbn]
                self.current_user.borrow_book(book)
            elif member_choice==2:
                self.current_user.show_all_books()
                isbn = input("enter isbn number to return: ")
                self.current_user.return_book(isbn)
            elif member_choice==3:
                self.current_user.show_all_books(isbn)


    def show_books(self):
        print("library has the following books:")
        for book in self.books:
            self.books[book].show_book()




