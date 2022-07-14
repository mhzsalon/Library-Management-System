book_name = []
author = []
quantity = []
price = []
def listSplit():
    global book_name
    global author
    global quantity
    global price

    stock = open("Books", "r")
    lines = stock.readlines()
    lines = [x.strip("\n")for x in lines]

    for i in lines:
        a = i.split(",")
        book_name.append(a[0])
        author.append(a[1])
        quantity.append(a[2])
        price.append(a[3])

listSplit()
