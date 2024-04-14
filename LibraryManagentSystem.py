book_list = []

def menu():
    print("Library Menu:")
    print("1. Create a book")
    print("2. Show books")
    print("3. Issue a book")
    print("4. Return a book")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter your choice : ")


    if choice == "1":
        book_name = input("Enter the name of the book: ")
        book_list.append(book_name)
        print(f"{book_name} has been added to the library.")
    elif choice == "2":
        print("Books in the library:")
        for book in book_list:
            print(book_list)
    elif choice == "3":
        book_issue = input("Enter the name of the book to issue: ")
        if book_issue in book_list:
            book_list.remove(book_issue)
            print(f"{book_issue} has been issued.")
        else:
            print(f"{book_issue} is not in the library.")
    elif choice == "4":
        book_return = input("Enter the name of the book to return: ")
        book_list.append(book_return)
        print(f"{book_return} has been returned.")
    elif choice == "5":
        print("Thanks for visiting !")
        break
    else:
        print("Invalid choice. Please enter a valid choice ")
