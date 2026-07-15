from book import Book
from members import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        
    def add_book(self, book):
        self.books.append(book)

    def exucute(self, remove_book):
        res = input("What do you want to do? (remove_book, search_book)")
        if res == "remove_book":
            remove_book()
        elif res == "search_book":
            search = input("Enter a book title to search: ")
            self.search_book(search)
        

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