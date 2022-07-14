import Date_time
import Split

# Function to return book
def return_book():
    # Input to open borrow txt file
    while True:
        print("\n---------------------- Return section ---------------------")
        borrower = input("\nEnter borrower's name: ")
        try:
            borrow_note = open(f"Borrow-{borrower}", "r")
            data = borrow_note.read()
            print(data)
            break
        except:
            print(f"Borrower with name {borrower} does not exist.")

    # text file creation for returning book
    return_note = open(f"Return-{borrower}", "w+")
    return_note.write("                             Library Management System\n")
    return_note.write(f"\n\tBorrowed by: {borrower}")
    return_note.write(f"\t\t\t\t\t\t Date: {Date_time.date()}\n")
    return_note.write(f"\t\t\t\t\t\t\t\t\t\t\t Time: {Date_time.time()}\n")
    return_note.write("\t---------------------------------------------------------------------\n")
    return_note.write("\t S.N.\t\t\t\t\t Book name \t\t\t\t\t Price \n")
    return_note.write("\t---------------------------------------------------------------------\n")

    total = 0.0
    for i in range(3):
        if Split.book_name[i] in data:
            return_note = open(f"Return-{borrower}", "a")
            return_note.write(f"\t {str(i)}. \t\t\t\t {Split.book_name[i]} \t\t\t\t\t {Split.price[i]}\n")
            Split.quantity[i] = int(Split.quantity[i]) + 1
            price = Split.price[i].replace("$", "")
            total += float(price)

    expire_date = input("Is your return date expired(Yes/No): ")
    if expire_date.lower() == "yes":
        late = int(input("How many days are you late: "))
        fine = 2 * late
        return_note = open(f"Return-{borrower}", "a")
        return_note.write("\t---------------------------------------------------------------------\n")
        return_note.write(f"\t\t\t\t\t Fine: \t\t\t\t\t\t\t ${fine}\n")
        total += fine
        return_note.write(f"\t\t\t\t\t Total: \t\t\t\t\t\t\t ${total}\n")
        return_note.write("\t---------------------------------------------------------------------\n")
        return_note.close()
        return_note = open(f"Return-{borrower}", "r")
        print(return_note.read())
    else:
        return_note = open(f"Return-{borrower}", "a")
        return_note.write("\t---------------------------------------------------------------------\n")
        return_note.write(f"\t\t\t\t\t\t\t Total: \t\t\t\t\t ${total}\n")
        return_note.write("\t---------------------------------------------------------------------\n")
        return_note = open(f"Return-{borrower}", "r")
        print(return_note.read())
