from book import Book
from members import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
    def add_member(self, member):
        self.members.append(member)
    def show_books(self):
        print("\n Books in Library: \n")
        for book in self.books:
            book.display()
            print("--------------------")
    def show_members(self):
        print("\n Members in Library: \n")
        for member in self.members:
                member.display()
                print("--------------------")