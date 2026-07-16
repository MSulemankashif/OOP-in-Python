from book import Book
from members import Member
from Library import Library
 

library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 12.99)
book3 = Book("1984", "George Orwell", 9.99)

member1 = Member("M Suleman", 22)
member2 = Member("Ayesha Khan", 25)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.add_member(member1)
library.add_member(member2)

library.show_books()
library.execute()

library.show_members()

# title = input("Enter book title to remove a book: ")
# library.remove_book(title)

search = input("Enter a book title to search: ")
library.search_book(search)
