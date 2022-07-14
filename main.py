import Borrow
import Return
import Split

while True:
    print("\n--------------------- Welcome To Library Management System -------------------")
    print("\nD : To display available books")
    print("B : To borrow book")
    print("R : To return book")
    print("E : To exit")

    # Taking user input
    user = input("\nChoose from above options: ")

    # Display's the books
    if user.lower() == "d":
        print("\n\t\t\t--*-*-*-*-*-*-*-*--Books Section--*-*-*-*-*-*-*-*--\n")
        print("-------------------------------------------------------------------------------------")
        print("S.N \t\t Book name \t\t\t\t Author \t\t Quantity \t\t Price")
        print("-------------------------------------------------------------------------------------")
        for i in range(3):
            print(f"{str(i)} \t\t\t {Split.book_name[i]} \t\t\t {Split.author[i]} \t\t {Split.quantity[i]} \t\t\t {Split.price[i]}")

    # Borrow books
    elif user.lower() == "b":
        Borrow.borrow()

    # Return books
    elif user.lower() == "r":
        Return.return_book()

    # Exit the program
    elif user.lower() == "e":
        print("Thank you for choosing our library")
        break

    else:
        print("Invalid input! Please choose from given options.")
