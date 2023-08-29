import time

# A list to store books
Books_List = []

class Book:
    def __init__(self, title, author, pubYear):
        self.title = title
        self.author = author
        self.pubYear = pubYear

    def __str__(self):
        return f"{self.title} by {self.author} (Published in {self.pubYear})"

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    pubYear = input("Enter the publication year: ")
    new_book = Book(title, author, pubYear)
    Books_List.append(new_book)
    print(f"Book {title} added!")

def removeBook():
    title = input("Enter the title of the book to remove: ")
    book_found = False
    for index, book in enumerate(Books_List):
        if book.title == title:
            del Books_List[index]
            print(f"Book {title} removed!")
            book_found = True
            break
    if not book_found:
        print("Book not found!")

def listAllBooks():
    for book in Books_List:
        print(book)
    time.sleep(2)  # Why is this here?

def searchBook():
    title = input("Enter the title of the book to search: ")
    for book in Books_List:
        if book.title == title:
            print(book)
            return
    print("Book not found!")

def updateBook():
    title = input("Enter the title of the book to update: ")
    for book in Books_List:
        if book.title == title:
            new_title = input("Enter the new title: ")
            new_author = input("Enter the new author's name: ")
            new_pubYear = input("Enter the new publication year: ")
            book.title = new_title if new_title else book.title
            book.author = new_author if new_author else book.author
            book.pubYear = new_pubYear if new_pubYear else book.pubYear
            print(f"Book {title} updated!")
            return
    print("Book not found!")

# Placeholder for the main execution loop, if needed
# while True:
#     # TODO: Add a menu for the user to interact with

