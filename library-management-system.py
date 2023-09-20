import time
import datetime

# A list to store books
# changed the name of the list too booksList from Books_List
booksList = []
# Added a dictionary to store borrowers
borrowList = {}

# User prompt to input number, returns an integer and prints an error message if the input is not a number
def inputNumber():
    num = input()
    while not num.isdigit():
        print("Invalid input. Please enter a number.")
        num = input()
    return int(num)

    

class Book:
    def __init__(self, title, author, pubYear):
        self.title = title
        self.author = author
        self.pubYear = pubYear
        self.borrower = None
        
    def borrow(self, borrower):
        if self.borrower:
            print("Book is already borrowed!")
            return
        self.borrower = borrower
        print(f"{borrower.name} borrowed {self.title} on {datetime.datetime.now()}")

    def __str__(self):
        return f"{self.title} by {self.author} (Published in {self.pubYear})"

# changed the name of the function to addBook from add_book
def addBook():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    pubYear = input("Enter the publication year: ")
    # changed the name of the variable to newBook from new_book
    newBook = Book(title, author, pubYear)
    booksList.append(newBook)
    print(f"Book {title} added!")

def removeBook():
    title = input("Enter the title of the book to remove: ")
    # changed the name of the variable to bookFound from book_found
    bookFound = False
    for index, book in enumerate(booksList):
        if book.title == title:
            del booksList[index]
            print(f"Book {title} removed!")
            bookFound = True
            break
    if not bookFound:
        print("Book not found!")

def listAllBooks():
    for book in booksList:
        print(book)
   
def searchBook():
    title = input("Enter the title of the book to search: ")
    for book in booksList:
        if book.title == title:
            print(book)
            return
    print("Book not found!")

def updateBook():
    title = input("Enter the title of the book to update: ")
    for book in booksList:
        if book.title == title:
            # changed the name of the variable to newTitle from new_title
            newTitle = input("Enter the new title: ")
            # changed the name of the variable to newAuthor from new_author
            newAuthor = input("Enter the new author's name: ")
            # changed the name of the variable to newPubYear from new_pubYear
            newPubYear = input("Enter the new publication year: ")
            book.title = newTitle if newTitle else book.title
            book.author = newAuthor if newAuthor else book.author
            book.pubYear = newPubYear if newPubYear else book.pubYear
            print(f"Book {title} updated!")
            return
    print("Book not found!")

class Member:
    def __init__(self, name, age, address, phone, email):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.email = email
        self.borrowedBooks = []

    def __str__(self):
        return f"{self.name} is {self.age} years old, lives at {self.address}, phone number is {self.phone}, and email is {self.email}"

    def addBook(self, book):
        self.borrowedBooks.append(book)
        print(f"{self.name} borrowed {book.title} on {datetime.datetime.now()}")

    def removedBook(self, book):
        self.borrowedBooks.remove(book)
        print(f"{self.name} returned {book.title} on {datetime.datetime.now()}")
        
class Borrower:
    def __init__(self, name, dateBorrowed, dateDue, dateReturned):
        self.name = name
        self.books = []

    def __str__(self):
        return f"{self.name} borrowed {self.book} on {self.dateBorrowed} and it is due on {self.dateDue}"

    def returnBook(self):
        self.book = None
        print(f"{self.name} returned the book on {self.dateReturned}")

def on_button_click():
    print("Button clicked!")

def createBorrower():
    name = input("Enter your name: ")
    if name in borrowList:
        print("Borrower already exists!")
        return
    borrower = Borrower(name, None, None, None, None)
    borrowList[name] = borrower
    print(f"created a borrower named {name}")

# Placeholder for the main execution loop, if needed
# while True:
#     # TODO: Add a menu for the user to interact with
while True:
    print("Welcome to the Library Management System")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. List all books")
    print("4. Search for a book")
    print("5. Update a book")
    print("6. Borrow a book")
    print("7. Return a book")
    print("8. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        addBook()
    elif choice == 2:
        removeBook()
    elif choice == 3:
        listAllBooks()
    elif choice == 4:
        searchBook()
    elif choice == 5:
        updateBook()
    elif choice == 6:
        Borrower.name = input("Enter your name: ")
    elif choice == 8:
        print("Thank you for using the Library Management System!")
        break
    else:
        print("Invalid choice!")

