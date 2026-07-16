from book import Book
from members import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        
    def add_book(self, book):
        self.books.append(book)

    def execute(self):
        res = input("What do you want to do? (remove_book, search_book, update_book)")
        if res == "remove_book":
            self.remove_book()
        elif res == "search_book":
            search = input("Enter a book title to search: ")
            self.search_book(search)
        elif res == "update_book":
            self.update_title()

    def update_title(self):
        title = input("Enter the title of the book you want to update: ")
        for book in self.books:
            if book.title == title:
                self.show_books()
                update = input("What do you want to update? (title, author, price)")
                if update == "title":
                    new_title = input("Enter the new title: ")
                    book.title = new_title
                    print(f"Book title update to '{new_title}'")
                elif update == "author":
                    new_author = input("Enter the new author: ")
                    book.author = new_author
                    print(f"Book author update to '{new_author}'")
                elif update == "price":
                    new_price = input("Enter the new price: ")
                    book.price = new_price
                    print(f"Book price update to '{new_price}'")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book '{title}' has been removed from the library")
                self.show_books()
                return
        print(f"Book '{title}' not found in library.")

    def search_book(self, search):
        found_books = []
        results = [book for book in self.books if search.lower() in book.title.lower()]
        if results:
            print(f"\n Search results for '{search}': \n")
            for book in results:
                book.display()
                print("--------------------")
        else:
            print(f"\n No Books found for '{search}' in Library")
         

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