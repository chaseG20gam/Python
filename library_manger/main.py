def check_library():

    book_library = open("books.txt", "r")
    print(book_library.read().splitlines())
    book_library.close()

def increase_library(new_book=""):

    book_library = open("books.txt", "a")
    new_book = input("Enter the name of the new book to add: ")
    
    if new_book:
        book_library.write(new_book + "\n")
        print(f"Added new book: {new_book}")
        book_library.close()
    else:
        print("No new book provided to add.")
    book_library.close()

def first_book_read():
    book_library = open("books.txt", "r")
    first_book = book_library.readline().strip()
    print(f"The first book in the library is: {first_book}")
    book_library.close()

def choice(choice):

    if choice == str(1):
        check_library()
    elif choice == str(2):
        increase_library()
    elif choice == str(3):
        first_book_read()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

if __name__ == "__main__":

    print("what do you want to do?")
    print("1. Check library")
    print("2. Increase library")
    print("3. Read first book")
    choice_ = input("Enter your choice (1, 2 or 3): ")

    choice(choice_)