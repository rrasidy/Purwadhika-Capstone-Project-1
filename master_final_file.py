dict_of_books = {1: {'ISBN' : '10001', 'Title' : 'How To Train Your Dragon', 'Author' : 'Cressida Cowel', 'Admin' : 'Robert'}, 
                 2: {'ISBN' : '10002', 'Title' : 'The Amazing Spider-man', 'Author' : 'Stan Lee', 'Admin' : 'Robert'}}

menuSelection = ""

Admins = ['Robert','Hakim']

loginAdmin = input("Enter your name (CASE SENSITIVE): ")

deletedBooks = {}

def my_search():
    total = 0
    searchKeyWord = input("What do you want to search? ")
    for k,v in dict_of_books.items():
        for x in v.values():
            if searchKeyWord.lower() in x.lower():
                print(k,v)
                total += 1
    print("Match Search found: {}".format(total))

def view_books():
    while True:
        print("1. View all books \n" "2. View a book by key \n" "3. Search by ISBN/Title/Author/Admin \n" "4. Exit back to menu")
        viewViewSelection = input("Enter the action you want to do: ")
        if viewViewSelection.isdigit():
            if int(viewViewSelection) == 1:
                for x,y in dict_of_books.items():
                    print(x,y)
                view_books()
            elif int(viewViewSelection) == 2:
                bookIDselection = input('''Enter the book you want to view using it's key: ''')
                if bookIDselection.isdigit():
                    ConfirmationBookIsThere = int(bookIDselection) in dict_of_books
                    if ConfirmationBookIsThere == True:
                            print("Details of selected book key {}: ".format(bookIDselection))
                            print(dict_of_books[int(bookIDselection)])
                    else:
                        print("Book does not exist")
                        view_books()
            elif int(viewViewSelection) == 3:
                my_search()
                view_books()
            elif int(viewViewSelection) == 4:
                my_menu()

def add_books():
    while True:
        print("1. Add a book \n" "2. Exit back to menu")
        addSelection = input("Enter the action you want to do: ")
        if addSelection.isdigit():
            if int(addSelection) == 1:
                addBookID = input('''Enter the new book's ISBN (ISBN MUST BE UNIQUE): ''')
                addBookName = input('''Enter the book's title: ''')
                addBookAuthor = input('''Enter the book's author: ''')
                addConfirmation = input ("Are you sure you want to add this book? (Y/N): ")
                if len(addBookID)>0 and len(addBookName)>0 and len(addBookAuthor)>0:
                    if addConfirmation.lower() == 'y':
                        List_dict_of_books = list(dict_of_books)
                        List_dict_of_books.sort()
                        UniqueNumberKey = List_dict_of_books[-1] + 1
                        add_dict_of_books = {
                            UniqueNumberKey  : {'ISBN' : addBookID, 'Title' : addBookName, 'Author' : addBookAuthor, 'Admin' : loginAdmin}
                    }
                        dict_of_books_values = dict_of_books.values()
                        isexist = False
                        for k in dict_of_books_values:
                                x = k['ISBN']
                                if addBookID != x:
                                    continue
                                else:
                                    print("Book ISBN needs to be unique")
                                    isexist = True
                                    break
                        if isexist == False:
                            dict_of_books.update(add_dict_of_books)
                            print("Book Sucesfully added to dictionary")
                    add_books()
                else:
                    print("Every information of the book for creation needs to be filled")
            elif int(addSelection) == 2:
                my_menu()

def Restore(parm=0):
    for (x,y) in deletedBooks.items():
        TrueRestore = False
        if parm == 0:
            TrueRestore = True
        else:
            if parm == x:
                TrueRestore = True
        if TrueRestore == True:
            add_dict_of_books = {max(dict_of_books) + 1 : y }
            dict_of_books.update(add_dict_of_books)
    return
                
    
def delete_books():
    while True:
        deleteSelection = ""
        print("1. Delete a book by key\n" "2. Showcase Deleted Books \n" "3. Restore deleted books \n" "4. Delete a book by search \n" "5. Exit back to menu")
        viewDeleteSelection = input("Enter the action you want to do: ")
        if viewDeleteSelection.isdigit():
            if int(viewDeleteSelection) == 1:
                for k,v in dict_of_books.items():
                    print(k,v)
                deleteSelection = input('''Enter the book key you want to delete (the key is number with integer type): ''')
                if deleteSelection.isdigit():
                    ConfirmationBookExists = int(deleteSelection) in dict_of_books
                    if ConfirmationBookExists == True:
                        confirmation = input("Are you sure you want to delete key number {}? (Y/N): ".format(deleteSelection))
                        if confirmation.isalpha():
                            if confirmation.lower() == "y":
                                deletedBooks[int(deleteSelection)] = dict_of_books[int(deleteSelection)]
                                del dict_of_books[int(deleteSelection)]
                                print("Succesfully deleted selected book key {}".format(deleteSelection))
                                delete_books()
                            elif confirmation.lower() == "n":
                                delete_books()
                    elif ConfirmationBookExists == False:
                        print("Book does not exist in dictionary")
                        delete_books()
            elif int(viewDeleteSelection) == 2:
                print("Showcasing deleted books....")
                if len(deletedBooks) == 0:
                    print("There was no books that had been deleted")
                    delete_books()
                else:
                    print(deletedBooks)
                    delete_books()
            elif int(viewDeleteSelection) == 3:
                if len(deletedBooks) == 0:
                    print("There was no books that had been deleted")
                    delete_books()
                else:
                    for (x,y) in deletedBooks.items():
                        print(x,y)
                        continue
                    print("1. Return all deleted books \n" "2. Cancel returning")
                    ReturningSelection = input("Please input the action you want to do: ")
                    if ReturningSelection.isdigit():
                        if int(ReturningSelection) == 1:
                            print("Returning all deleted books to the library..")
                            Restore()
                            deletedBooks.clear()
                            print("SUCCESS!")
                            delete_books()
                        else:
                            delete_books()
            elif int(viewDeleteSelection) == 4:
                total = 0
                searchDelete = input("What do you want to search for deletion: ")
                for k,v in dict_of_books.items():
                    for x in v.values():
                        if searchDelete.lower() in x.lower():
                            print(k,v)
                            total += 1   
                if total == 0:
                    print("Match Search found: {}".format(total))
                    print("No book met the search criteria, returning back to delete menu...")
                    delete_books()
                else:
                    print("Match Search found: {}".format(total))
                    DeleteSelect = input("Which book (by key) out of the search do you want to delete: ")
                    if DeleteSelect.isdigit():
                        if DeleteSelect in str(k):
                            deletedBooks[int(DeleteSelect)] = dict_of_books[int(DeleteSelect)]
                            del dict_of_books[int(DeleteSelect)]
                            print("Succesfully deleted book")
                            delete_books()
                        else:
                            print("Book out of the search criteria")
                            delete_books()
            else:
                my_menu()

def update_books():
    while True:
        print("1. Update information about a book \n" "2. Exit back to menu")
        updateBookSelection = input("What action do you want to do: ")
        if updateBookSelection.isdigit():
            if int(updateBookSelection) == 1:
                for x,y in dict_of_books.items():
                    print(x,y)
                NumberBookSelection = input("Enter which book you want to update by key: ")
                if NumberBookSelection.isdigit():
                    ConfirmationBookExists = int(NumberBookSelection) in dict_of_books
                    if ConfirmationBookExists == True:
                        print(dict_of_books[int(NumberBookSelection)])
                        confirmationUpdate = input("Are you sure this is the book you want to update? (Y/N): ")
                        if confirmationUpdate.isalpha():
                            if confirmationUpdate.lower() == 'y':
                                BookPartUpdate = input("Which part of the book do you want to update: ")
                                if BookPartUpdate.lower() == 'admin':
                                    print("This field can not be updated manually")
                                    update_books()
                                elif BookPartUpdate.lower() == 'isbn' or 'author' or 'title':
                                    UpdatingBook = input("What do you want to change it into: ")
                                    if len(BookPartUpdate)>0 and len(UpdatingBook)>0:
                                        dict_of_books[int(NumberBookSelection)][BookPartUpdate.capitalize()] = '{}'.format(UpdatingBook)
                                        dict_of_books[int(NumberBookSelection)]['Admin'] = '{}'.format(loginAdmin)
                                        print("Succesfully updated by {}".format(loginAdmin))
                                    else:
                                        print("Every Criteria needs to be filled for updation")
                                else:
                                    print("Please input a part that is in the selected book")
                                    update_books()
                            update_books()
                    else:
                        print("Book is not in list")
                        update_books()
            elif int(updateBookSelection) == 2:
                my_menu()

def cek_login():
    CheckAuthorization = loginAdmin in Admins
    if CheckAuthorization == False:
        print("Unauthorized User")
        return False
    else:
        return True
## Authorized users is in Admins list
    
def my_menu():
    while True:
        print ("Halo {} Selamat datang ke perpustakaan".format(loginAdmin))
        print(
            "1. View every book \n"
            "2. Add a new book \n"
            "3. Delete a book \n"
            "4. Update a book \n"
            "5. Exit")
        menuSelection = input("What action do you want to do: ")
        if menuSelection.isdigit():
            if int(menuSelection) == 1:
                view_books()
            elif int(menuSelection) == 2:
                add_books()
            elif int(menuSelection) == 3:
                delete_books()
            elif int(menuSelection) == 4:
                update_books()
            elif int(menuSelection) == 5:
                print("Thank you for visiting, {}".format(loginAdmin))
                exit()

if cek_login() == True:
    while my_menu() != 5:
        my_menu() 