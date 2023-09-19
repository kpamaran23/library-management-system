import time

# A list to store books
#changed the name of the list too booksList from Books_List
booksList = []

class Book:
    def __init__(self, title, author, pubYear):
        self.title = title
        self.author = author
        self.pubYear = pubYear

    def __str__(self):
        return f"{self.title} by {self.author} (Published in {self.pubYear})"

#changed the name of the function to addBook from add_book
def addBook():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    pubYear = input("Enter the publication year: ")
    #changed the name of the variable to newBook from new_book
    newBook = Book(title, author, pubYear)
    booksList.append(newBook)
    print(f"Book {title} added!")

def removeBook():
    title = input("Enter the title of the book to remove: ")
    #changed the name of the variable to bookFound from book_found
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
    time.sleep(2)  # Why is this here?

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

while True:
    print("Welcome to the Library Management System")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. List all books")
    print("4. Search for a book")
    print("5. Update a book")
    print("6. Exit")
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
        print("Thank you for using the Library Management System!")
        break
    else:
        print("Invalid choice!")

