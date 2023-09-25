# Added a datetime modulebookslist
# Taken from https://www.w3schools.com/python/python_datetime.asp
import datetime

# User prompt to input number, returns the integer
# or the value entered and prints an error message if the input
# is not a number or is invalid.
def input_number():
    num = input()
    while not num.isdigit():
        print("Invalid input. Please enter a number.")
        num = input()
    return int(num)

# Asks user for a string which can be a
# member name or a book name
def input_string():
    return input()

# The Book class will inherit from the LibraryItem parent class
class Book():
    # Changed pubYear to pub_date
    def __init__(self, title, author, pub_date):
        # Added a constructor of the LibraryItem parent class
        self.title = title
        self.author = author
        self.pub_date = pub_date
        # added a borrower and due date attribute and initialising them to None.
        self.borrower = None
        self.due_date = None
    
    def display_info(self):
        return f"Title: {self.title} by {self.author} (Published in {self.pub_date})"

    def __str__(self):
        return "Title:" f"{self.title} by {self.author} (Published in {self.pub_date})"

    def is_borrowed(self):
        return self.borrower is not None
    
    def set_due_date(self, due_date):
        self.due_date = due_date

# # The Member class will inherit from the LibraryItem parent class
class Member():
    def __init__(self, name):
        self.name= name
        self.borrowed_books = []

    def display_info(self):
        borrowed_books_info = ', '.join(book.title for book in self.borrowed_books)
        return f"Name: {self.title}, Books borrowed: {borrowed_books_info}"
    
    def __str__(self):
        books_combined = []
        for i in self.borrowed_books:
            books_combined.append(i.__str__())
        
        return "Name: " f"{self.name}, Books borrowed: {' '.join(books_combined)}"
    
    def add_book(self, book):
        self.borrowed_books.append(book)
    
    def remove_book(self, book):
        self.borrowed_books.remove(book)

# A Library class to store books and members
class Library:
    def __init__(self):
        self.books = []
        self.members_list = []

    def add_member(self, name):
        if not self.check_member(name):
            self.members_list.append(Member(name))
        else:
            print("Member already exists")

    # Call this function to check if a member exists
    # Returns false if the member is not in the 
    # membersList and true if otherwise
    def check_member(self, name):
        exists = False
        for mem in self.members_list:
            if mem.name == name:
                exists = True
                return exists
        return exists

    # Call this function to check if a book exists
    # Returns false if the book is not in the books list
    # and true if otherwise
    def check_book(self, book):
        exists = False
        for bk in self.books:
            if bk.title == book:
                exists = True
                return exists
        return exists

    def remove_member(self, name):
        if self.check_member(name):

            for mem in self.members_list:
                if mem.name == name:
                    if len(mem.borrowed_books) > 0:
                        print("Member has borrowed books. Cannot remove member")
                        return
                    self.members_list.remove(mem)
                    print("Member removed: " + mem.__str__())
                    return
        else:
            print("Member does not exist")

# Added a parameter to the function to accept the book object
    def add_book(self, title, author, pub_year):
        if not self.search_book(title):
            new_book = Book(title, author, pub_year)
            self.books.append(new_book)
            print(f"Book {title} added!")
            return
        else:
            print("Book already exists")
            
        

    def remove_book(self, title):
        book_found = False
        for index, book in enumerate(self.books):
            if book.title == title and book.borrower is None:
                del self.books[index]
                print(f"Book {title} removed!")
                book_found = True
        if not book_found:
            print("Book not found or is borrowed!")

    def borrowed_book(self, book, member):
        if not self.check_book(book):
            print("Book does not exist")
            return
        elif not self.check_member(member):
            print("Member does not exist")
            return
        
        # Generated from Chat-GPT
        for bk in self.books:
            if bk.title == book and bk.borrower is None:
                mem = self.search_member(member)
                bk.borrower = mem
                mem.add_book(bk)
                due_date = datetime.date.today() + datetime.timedelta(days=14)
                bk.set_due_date(due_date)
                print(mem.name + " Book borrowed: " + bk.__str__())
                print("Due date: " + bk.due_date.__str__() + "\n")
                return  
        print("Book not found")


    def return_book(self, book, member):
        if not self.check_book(book):
            print("Book does not exist")
            return
        elif not self.check_member(member):
            print("Member does not exist")
            return
        
        mem = self.search_member(member)
        bk = self.search_book(book)
        if bk is not None and bk.borrower is not None and bk.borrower.name == mem.name:
            bk.borrower = None
            mem.remove_book(bk)
            print("Book returned:" + bk.__str__())
        else:
            print("Book is not borrowed by " + mem.name)
            
    def list_all_books(self):
        print("Books in library:" + str(len(self.books)))
        for book in self.books:
            print(book.__str__())

    # Added a function to list all members
    def list_all_members(self):
        print("Count of Members in Library: " + str(len(self.members_list)))
        for mem in self.members_list:
            print(mem.__str__())

   # Added a function to search for the name of a member
    def search_member(self, member):
        for mem in self.members_list:
            if mem.name == member:
                return mem
        print("No member found for " + member)

    # Added a function to search for a book        
    def search_book(self, book):
        for bk in self.books:
            if bk.title == book:
                return bk      
        print("No book found for " + book) 
        return None

    def update_book(self, title, new_title, new_author, new_pub_year):
        for book in self.books:
            if book.title == title:
                book.title = new_title if new_title else book.title
                book.author = new_author if new_author else book.author
                book.pub_year = new_pub_year if new_pub_year else book.pub_year
                print(f"Book {title} updated!")
                return
        print("Book not found!")

    # Added a function to check for overdue books
    def check_overdue_books(self):
        print("Overdue books: ")
        for book in self.books:
            if book.due_date < datetime.date.today():
                print(book.title)

class LibraryConsole:
    def __init__(self, library):
        self.library = library

    def start(self):
        print("Welcome to the library")
        while True:
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

            choice = input_number()

            if choice == 1:
                name = input_string()
                self.library.add_member(name)
            # Add similar logic for other menu choices
            elif choice == 13:
                self.display_menu()
            elif choice == 14:
                print("Goodbye!")
                break
            else:
                print("Invalid input")

    def display_menu(self):
        # Print the menu without asking for input
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

def input_number():
    num = input()
    while not num.isdigit():
        print("Invalid input. Please enter a number.")
        num = input()
    return int(num)

def input_string():
    return input()

def main():
    # Create an instance of the Library class
    library = Library()

# Added a menu for the user to interact with
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
    choice = input_number()

    if choice == 1:
        print("Enter member name to add: ")
        name = input_string()
        lib.add_member(name)
    elif choice == 2:
        print("Enter member name to remove: ")
        name = input_string()
        lib.remove_member(name)
    elif choice == 3:
        print("Enter book title to add: ")
        title = input_string()
        print("Enter book author: ")
        author = input_string()
        print("Enter book publication year: ")
        pub_year = input_number()
        lib.add_book(title, author, pub_year)
    elif choice == 4:
        print("Enter book title to remove: ")
        title = input_string()
        lib.remove_book(title)
    elif choice == 5:
        print("Enter book title to borrow: ")
        book = input_string()
        print("Enter member name to borrow: ")
        member = input_string()
        lib.borrowed_book(book, member)
    elif choice == 6:
        print("Enter book title to return: ")
        book = input_string()
        print("Enter member name to return: ")
        member = input_string()
        lib.return_book(book, member)
    elif choice == 7:
        lib.list_all_members()
    elif choice == 8:
        lib.list_all_books()
    elif choice == 9:
        print("Enter book title to update: ")
        title = input_string()
        print("Enter new book title:")
        new_title = input_string()
        print("Enter new book author: ")
        new_author = input_string()
        print("Enter new book publication year: ")
        new_pub_year = input_number()
        lib.update_book(title, new_title, new_author, new_pub_year)
    elif choice == 10:
        lib.check_overdue_books()
    elif choice == 11:
        print("Enter book title to search: ")
        title = input_string()
        lib.search_book(title)
    elif choice == 12:
        print("Enter member name to search: ")
        name = input_string()
        lib.search_member(name)


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
