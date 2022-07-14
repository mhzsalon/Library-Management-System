import Date_time
import Split

def borrow():
    print("\n---------------------- Borrow section ---------------------")
    print("Note : You cannot borrow the same book twice. ")

    # First name of borrower
    while True:
        firstName = input("\nEnter your first name: ")
        if firstName.isalpha():
            break
        print("You cannot enter numbers or special characters! ")

    # last name of borrower
    while True:
        lastName = input("Enter your last name: ")
        if lastName.isalpha():
            break
        print("You cannot enter numbers or special characters! ")

    # Creating txt file
    borrow_note = open(f"Borrow-{firstName}", "w+")
    borrow_note.write("                             Library Management System\n")
    borrow_note.write(f"\n\tBorrowed by: {firstName} {lastName}")
    borrow_note.write(f"\t\t\t\t\t\t Date: {Date_time.date()}\n")
    borrow_note.write(f"\t\t\t\t\t\t\t\t\t\t\t Time: {Date_time.time()}\n")
    borrow_note.write("\t---------------------------------------------------------------------\n")
    borrow_note.write("\t S.N.\t\t\tBook name \t\t\t Author \t\t\t Price\n")
    borrow_note.write("\t---------------------------------------------------------------------\n")

    while True:
        print("\n           Please select a book from the following options:")
        # Loop to display book name
        for i in range(len(Split.book_name)):
            print(f"Press {i} to borrow {Split.book_name[i]}")

        # Input to borrow book
        try:
            while True:
                num = int(input("Input: "))
                if num >= 0:
                    if num <= len(Split.book_name)-1:
                        if int(Split.quantity[num]) > 0:
                            print("Book is available.")
                            borrow_note = open(f"Borrow-{firstName}", "a")
                            borrow_note.write(f"\t 1.\t\t\t {Split.book_name[num]} \t\t\t {Split.author[num]} \t\t {Split.price[num]}\n ")

                            # Updating stocks
                            Split.quantity[num] = int(Split.quantity[num]) - 1
                            borrow_note = open("Books", "w+")
                            for i in range(len(Split.book_name)):
                                borrow_note.write(f"{Split.book_name[i]},{Split.author[i]},{str(Split.quantity[i])},{Split.price[i]}\n")
                        else:
                            print("Book is not available.")
                        break
                    else:
                        print(f"The provided input does not exist.")
                else:
                    print("The input cannot be negative value.")
        except:
            print("Invalid! input")

        # Borrow multiple book
        confirm = input("\nWould do like to borrow other books(Yes/No): ")
        if confirm.lower() == "no":
            borrow_note = open(f"Borrow-{firstName}", "r")
            print(borrow_note.read())
            print("\n \t\tThank you for borrowing with us.")
            break

