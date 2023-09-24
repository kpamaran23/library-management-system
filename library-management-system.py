# Added a datetime modulebookslist
import datetime


# User prompt to input number, returns the integer
# or the value entered and prints an error message if the input
# is not a number.
def inputNumber():
    Num = input()
    while not Num.isdigit():
        print("Invalid input. Please enter a number.")
        Num = input()
    return int(Num)

# Asks user for a string which can be a
# member name or a book name
def inputString():
    return input()


class Book:
    # Changed pubYear to pubDate
    def __init__(self, title, author, pubDate):
        self.title = title
        self.author = author
        self.pubDate = pubDate
        # added a borrower and due date attribute and initialising them to None.
        self.borrower = None
        self.dueDate = None
    
    def __str__(self):
        return "Title:" f"{self.title} by {self.author} (Published in {self.pubDate})"

    def isBorrowed(self):
        return self.borrower is not None
    
    def setDueDate(self, dueDate):
        self.dueDate = dueDate


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowedBooks = []

    def __str__(self):
        booksCombined = []
        for i in self.borrowedBooks:
            booksCombined.append(i.__str__())
        
        return "Name: " f"{self.name}, Books borrowed: {' '.join(booksCombined)}"
    
    def addBook(self, book):
        self.borrowedBooks.append(book)
    
    def removeBook(self, book):
        self.borrowedBooks.remove(book)

class Library:
    def __init__(self):
        self.books= []
        self.membersList = []

    def addMember(self, name):
        if self.checkMember(name) == False:
            self.membersList.append(Member(name))
        else:
            print("Member already exists")

    # Call this function to check if a member exists
    # Returns false if the member is not in the 
    # membersList and true if otherwise
    def checkMember(self, name):
        exists = False
        for mem in self.membersList:
            if mem.name == name:
                exists = True
                return exists
        return exists

    # Call this function to check if a book exists
    # Returns false if the book is not in the books list
    # and true if otherwise
    def checkBook(self, book):
        exists = False
        for bk in self.books:
            if bk.title == book:
                exists = True
                return exists
        return exists

    def removeMember(self, name):
        if self.checkMember(name) == True:

            for mem in self.membersList:
                if mem.name == name:
                    if len(mem.borrowedBooks) > 0:
                        print("Member has borrowed books. Cannot remove member")
                        return
                    self.membersList.remove(mem)
                    print("Member removed: " + mem.__str__())
                    return
        else:
            print("Member does not exist")

# changed the name of the function to addBook from add_book
# Added a parameter to the function to accept the book object
    def addBook(self, title, author, pubYear):
        if self.searchBook(title) != None:
            print("Book already exists")
            return
        # changed the name of the variable to newBook from new_book
        newBook = Book(title, author, pubYear)
        self.books.append(newBook)
        print(f"Book {title} added!")

    def removeBook(self, title):
        # changed the name of the variable to bookFound from book_found
        bookFound = False
        for index, book in enumerate(self.books):
            if book.title == title and book.borrower is None:
                del self.books[index]
                print(f"Book {title} removed!")
                bookFound = True
        if not bookFound:
            print("Book not found or is borrowed!")

    def borrowBook(self, book, member):
        if self.checkBook(book) == False:
            print("Book does not exist")
            return
        elif self.checkMember(member) == False:
            print("Member does no exist")
            return
        
        for bk in self.books:
            if bk.title == book and bk.borrower is None:
                mem = self.searchMember(member)
                bk.borrower = mem
                mem.addBook(bk)
                bk.setDueDate(datetime.date.today() + datetime.timedelta(days=14))
                print(mem.name + "Book borrowed: " + bk.__str__())
                print("Due date: " + bk.dueDate.__str__() + "\n")
                return
        print("Book not found")


    def returnBook(self, book, member):
        if self.checkBook(book) == False:
            print("Book does not exist")
            return
        elif self.checkMember(member) == False:
            print("Member does no exist")
            return
        
        mem = self.searchMember(member)
        bk = self.searchBook(book)
        if bk is not None and bk.borrower is not None and bk.borrower.name == mem.name:
            bk.borrower = None
            mem.removeBook(bk)
            print("Book returned:" + bk.__str__())
        else:
            print("Book is not borrowed by " + mem.name)
            
    def listAllBooks(self):
        print("Books in library:" + str(len(self.books)))
        for book in self.books:
            print(book.__str__())

    # Added a function to list all members
    def listAllMembers(self):
        print("Count of Members in Library: " + str(len(self.membersList)))
        for mem in self.membersList:
            print(mem.__str__())

   # Added a function to search for the name of a member
    def searchMember(self, member):
        for mem in self.membersList:
            if mem.name == member:
                return mem
        print("No member found for " + member)

    # Added a function to search for a book        
    def searchBook(self, book):
        for bk in self.books:
            if bk.title == book:
                return bk      
        print("No book found for " + book) 
        return None

    def updateBook(self, title, newTitle, newAuthor, newPubYear):
        for book in self.books:
            if book.title == title:
                book.title = newTitle if newTitle else book.title
                book.author = newAuthor if newAuthor else book.author
                book.pubYear = newPubYear if newPubYear else book.pubYear
                print(f"Book {title} updated!")
                return
        print("Book not found!")

    # Added a function to check for overdue books
    def checkOverDueBooks(self):
        print("Overdue books: ")
        for book in self.books:
            if book.dueDate < datetime.date.today():
                print(book.title)
# while True:
# TODO: Add a menu for the user to interact with
print("Welcome to the library")
print("1. Add a member")
print("2. Remove a member")
print("3. Add a book")
print("4. Remove a book")
print("5. Borrow a book")
print("6. Return a book")
print("7. List members")
print("8. List books")
print("9. Update a book")
print("10. Check overdue books")
print("11. Search for a book")
print("12. Search for a member")
print("13. Display menu")
print("14. Exit")
lib = Library()       
isRunning = True
while isRunning:
    print("Enter your choice: ")
    choice = inputNumber()

    if choice == 1:
        print("Enter member name to add: ")
        name = inputString()
        lib.addMember(name)
    elif choice == 2:
        print("Enter member name to remove: ")
        name = inputString()
        lib.removeMember(name)
    elif choice == 3:
        print("Enter book title to add: ")
        title = inputString()
        print("Enter book author: ")
        author = inputString()
        print("Enter book publication year: ")
        pubYear = inputNumber()
        lib.addBook(title, author, pubYear)
    elif choice == 4:
        print("Enter book title to remove: ")
        title = inputString()
        lib.removeBook(title)
    elif choice == 5:
        print("Enter book title to borrow: ")
        book = inputString()
        print("Enter member name to borrow: ")
        member = inputString()
        lib.borrowBook(book, member)
    elif choice == 6:
        print("Enter book title to return: ")
        book = inputString()
        print("Enter member name to return: ")
        member = inputString()
        lib.returnBook(book, member)
    elif choice == 7:
        lib.listAllMembers()
    elif choice == 8:
        lib.listAllBooks()
    elif choice == 9:
        print("Enter book title to update: ")
        title = inputString()
        print("Enter new book title:")
        newTitle = inputString()
        print("Enter new book author: ")
        newAuthor = inputString()
        print("Enter new book publication year: ")
        newPubYear = inputNumber()
        lib.updateBook(title, newTitle, newAuthor, newPubYear)
    elif choice == 10:
        Library.checkOverDueBooks()
    elif choice == 11:
        print("Enter book title to search: ")
        title = inputString()
        lib.searchBook(title)
    elif choice == 12:
        print("Enter member name to search: ")
        name = inputString()
        lib.searchMember(name)


    elif choice == 13:
        print("1. Add a member")
        print("2. Remove a member")
        print("3. Add a book")
        print("4. Remove a book")
        print("5. Borrow a book")
        print("6. Return a book")
        print("7. List members")
        print("8. List books")
        print("9. Update a book")
        print("10. Check overdue books")
        print("11. Search for a book")
        print("12. Search for a member")
        print("13. Display menu")
        print("14. Exit")
    elif choice == 14:
        isRunning = False
        print("Goodbye!")
    else:
        print("Invalid input")
