'''Implement a student library system using OOPs where student can borrow a book from list of tool.
crete a seperate library and student class. your program must be menu driven. you are free to choose
methods and attributes of your choice to implement the functionality.'''


class library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailablebooks(self):
        print("The books present in this library are : ")
        for book in self.books:
            print(" *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName} . Please keep it safe and make sure to return in 30 days ")
            self.books.remove(bookName)
            return True
        else:
            print("This book is already booked to someone. Please wait!")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning book. Hope you loved reading this.")

class Student: 
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

if __name__ == "__main__":
    centralLibrary = library(["Django", "Python", "Javascript", "Pascal"])
    Student = Student()
    # centralLibrary.displayAvailablebooks()
    while (True):
        welcomeMsg = '''\n **** WELCOME TO THE LIBRARY****
        Please choose an option:
        1. List of books
        2. Request a book
        3. Request to return a book
        4. Exit the library'''

        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailablebooks()
        elif a == 2:
            centralLibrary.borrowBook(Student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(Student.returnBook())
        elif a == 4:
            print("Thanks for choosing  library, Have a very good day")
        else:
            print("Invalid choices")

