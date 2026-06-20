import random
import json
import datetime



#==============File  Save and Load ======================
# now lets work on file handling for this json
def saveData(filename,data):
    with open(f"{filename}.json",'w') as f:
        data = json.dumps(data)
        f.write(data)

def loadData(filename):
    try:
        with open(f"{filename}.json",'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return {}
        

# =======================ADD book Function =====================
# first lets create every function separtely then combine
# add book to the libarary
# we will store the books in json file

def addbook(publishers,books):
    newbook = []
    title = input("Book Title : ")
    authorName = input("Author : ")
    category = input(r"Category (e.g Fiction/ Computer Science etc) : ")
    publisher = input("Publisher Name: ")
    countryCode = input("Country Code : ")
    # if country is 3 digits no need to add 0 at start if not add zeros eg 092 or 001
    # I think I have to generate ISBN using random then what I have to to is insert some how the dashes but dashes are not neccessory since it will be stored on database
    # It is my world and I have to create my own rules
    # it will be 13 digits isbn and first 3 for will for countrycode, next 4 will be publisher ( we will take the publihser
    # name and then generate a unique code publisher and remember to lower everyting) and last 6 will be for the title of the book random generated 


    # country code fix
    if len(countryCode) < 3:
        if len(countryCode) == 2:
            countryCode = "0"+countryCode
        else:
            countryCode = "00"+countryCode

    
    pubCode = 0
    if publisher not in publishers.values():
        pubCode = random.randint(1111,9999)
        publishers[pubCode] = publisher
        
    else:
        items = publishers.items()
        for i,j in items:
            if j == publisher:
                pubCode = i
    # what I have to do now generated title code
    titleCode = random.randint(111111,999999)

    ISBN = countryCode + str(pubCode) + str(titleCode)


    # now lets create a list for the book details 
    
    newbook.append(ISBN)
    newbook.append(title)
    newbook.append(authorName)
    newbook.append(category)
    newbook.append(publisher)

    books[ISBN] = newbook

    return "Books Successfully added to libarary"

    


# ============we have to create sign up and login () function

# we have to create a file in which login details will be stored and in form of json

def registerAccount(accounts):
    name = input("Name : ")
    email = input("Email Address : ")
    address = input("Address : ")
    pin = input("Enter 4 digit pin  ")
    assert len(pin) == 4
    
    try:
        m = max(accounts.keys())
    except ValueError:
        m = 100

    accounts[m+1] = [name,email,address,pin]

#===============Search Book Function===================
def searchBook(books):
    book = input("Book Name : ").lower()
    result = 0
    for i,j in books.items():
        if j[1].lower() == book:
            result = books[i]
            break

    if result == 0:
        result = "Book not found"
        return result 
    else:
        return result

# ==================Verify Borrower ====================
# verify borrower
def verifyBorrower(borrowerName,PIN,accounts):
    UsrDetails = 0
    for item in accounts.items():
        if borrowerName and PIN in item[1]:
            UsrDetails = accounts[item[0]]

    if UsrDetails == 0:
        return "User Not Found"
    else:
        return UsrDetails


# =======================Borrow Book ==========================
def borrowBook(borrowedbooks ,accounts,books):
    # yahan par verfication system lagani hai
    book = searchBook(books)
    if book != "Book not found":
        print(f"{book}")
        print("\n")
        
        ans = input("Do you want to borrow this book (Y/N) : ")
        borrowerName = input("Enter your username : ")
        borrowerPin = input("Enter account PIN : ")

        try:
            BID = len(borrowedbooks.keys())
        except ValueError:
            BID = 0
            
        if ans.lower not in  ["not","NOT","N","n"] :
            borrowDate = datetime.datetime.now()
            User = verifyBorrower(borrowerName,borrowerPin,accounts)
            print(User)
            
            if User != "User Not Found":
                Book_Borrowed = {
                    "Book" : book,
                    "BorrowDate": str(borrowDate),
                    "Borrower":User
                                }
                borrowedbooks[BID+1] = Book_Borrowed
                print("Book Borrowed Successfully")          
    else:
        return f"{book}"



books = dict(loadData("books"))
publishers = dict(loadData("publishers"))
accountsDetails = dict(loadData("accountsDetails"))
borrowedbooks = dict(loadData("borrowedbooks"))
if __name__ == "__main__":
    

    while True:
        print("=======================Le Welcome====================")
        print("1. Register Account")
        print("2. Add New To Library")
        print("3. Search Book In Library")
        print("4. Borrow Book")
        print("5. Quit")

        choice = int(input("Choice : "))

        if choice == 1:
            registerAccount(accountsDetails)
        elif choice == 2:
            addbook(publishers=publishers,books=books)
        elif choice == 3:
            searchBook(books)
        elif choice == 4:
            borrowBook(borrowedbooks,accountsDetails,books)
        elif choice == 5:
            saveData("books",books)
            saveData("accountsDetails",accountsDetails)
            saveData("publishers",publishers)
            saveData("borrowedbooks",borrowedbooks)
            
            break
