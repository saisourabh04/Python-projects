class Book:
    def __init__(self,isbn=None,title=None,author=None,no_of_copies=None):
        self.isbn=isbn
        self.title=title
        self.author=author
        self.no_of_copies=no_of_copies

    def show_book(self):
        print(f"book_details \nISBN:{self.isbn}\nTitle:{self.title}\nAuthor:{self.author}\nNo.of.Copies:{self.no_of_copies}")

