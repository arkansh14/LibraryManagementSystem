import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

# Function to add a new book
def addNewBook():
    bookid = int(input("Enter a book id : "))
    title = input("Enter book title : ")
    author = input("Enter author of the book : ")
    publisher = input("Enter book publisher : ")
    edition = input("Enter edition of book : ")
    cost = int(input("Enter cost of the book : "))
    category = input("Enter category of book : ")
    bdf = pd.read_csv(r"C:/Users/arkan/Desktop/books.csv", encoding='latin1')
    n = bdf["bookid"].count()
    bdf.at[n] = [bookid, title, author, publisher, edition, cost, category]
    bdf.to_csv(books_path, index=False)
    print("Book added successfully")

# Function to search for a book
def searchBook():
    name = input("Enter book title to be searched : ")
    bdf = pd.read_csv(r"C:/Users/arkan/Desktop/books.csv", encoding='latin1')
    df = bdf.loc[bdf["title"] == name]
    if df.empty:
        print("No book found with given title")
    else:
        print("Book details are ")
        print(df)

# Function to delete a book
def deleteBook():
    name = input("Enter book title to be deleted : ")
    bdf = pd.read_csv(r"C:/Users/arkan/Desktop/books.csv", encoding='latin1')
    bdf = bdf.drop(bdf[bdf["title"] == name].index)
    bdf.to_csv(r"C:/Users/arkan/Desktop/books.csv", index=False)
    print("Book Deleted Successfully")

# Function to show all books
def showBooks():
    bdf = pd.read_csv(r"C:/Users/arkan/Desktop/books.csv", encoding='latin1')
    print(bdf)

# Function to add a new member
def addNewMember():
    mid = int(input("Enter Member id : "))
    name = input("Enter name of the member : ")
    phone = input("Enter phone number : ")
    email = input("Enter email id : ")
    address = input("Enter address : ")
    number = 0
    mdf = pd.read_csv(r"C:/Users/arkan/Desktop/members.csv", encoding='latin1')
    n = mdf["Memberid"].count()
    mdf.at[n] = [mid, name, phone, email, address, number]
    mdf.to_csv(r"C:/Users/arkan/Desktop/members.csv", index=False)
    print("Member added successfully")

# Function to search for a member
def searchMember():
    name = input("Enter member name to be searched : ")
    mdf = pd.read_csv(r"C:/Users/arkan/Desktop/members.csv", encoding='latin1')
    df = mdf.loc[mdf["name"] == name]
    if df.empty:
        print("No member found with given name")
    else:
        print("Member details are ")
        print(df)

# Function to delete a member
def deleteMember():
    name = input("Enter member name to be deleted : ")
    mdf = pd.read_csv(r"C:/Users/arkan/Desktop/members.csv", encoding='latin1')
    mdf = mdf.drop(mdf[mdf["name"] == name].index)
    mdf.to_csv(r"C:/Users/arkan/Desktop/members.csv", index=False)
    print("Member Deleted Successfully")

# Function to show all members
def showMembers():
    mdf = pd.read_csv(r"C:/Users/arkan/Desktop/members.csv", encoding='latin1')
    print(mdf)

# Function to issue a book
def issueBook():
    bname = input("Enter Book name to be issued : ")
    df = pd.read_csv(r"C:/Users/arkan/Desktop/books.csv", encoding='latin1')
    df = df.loc[df["title"] == bname]
    if df.empty:
        print("No Book Found in the Library")
        return

    mname = input("Enter member name to be issued : ")
    df = pd.read_csv(r"C:/Users/arkan/Desktop/members.csv", encoding='latin1')
    df = df.loc[df["name"] == mname]
    if df.empty:
        print("No such Member Found")
        return

    idf = pd.read_csv(r"C:/Users/arkan/Desktop/issuedbooks.csv", encoding='latin1')
    book_issue = [bname, mname, date.today(), ""]
    n = idf["book_name"].count()
    idf.at[n] = book_issue
    idf.to_csv(r"C:/Users/arkan/Desktop/issuedbooks.csv", index=False)
    print("Book Issued Successfully")

# Function to show all issued books
def showIssuedBooks():
    idf = pd.read_csv(r"C:/Users/arkan/Desktop/issuedbooks.csv", encoding='latin1')
    print(idf)

# Function to return a book
def returnBook():
    bname = input("Enter Book to be returned : ")
    mname = input("Enter Member who has the book : ")
    idf = pd.read_csv(r"C:/Users/arkan/Desktop/issuedbooks.csv", encoding='latin1')
    idf = idf.loc[idf["book_name"] == bname]
    if idf.empty:
        print("The book is not issued in records")
    else:
        idf = idf.loc[idf["member_name"] == mname]
        if idf.empty:
            print("The book is not issued to the member")
        else:
            print("Book can be returned")
            ans = input("Are you sure you want to return the book : ")
            if ans.lower() == "yes":
                idf = pd.read_csv(r"C:/Users/arkan/Desktop/issuedbooks.csv", encoding='latin1')
                idf = idf.drop(idf[idf["book_name"] == bname].index)
                idf.to_csv(r"C:/Users/arkan/Desktop/issuedbooks.csv", index=False)
                print("Book Returned Successfully")
            else:
                print("Return operation cancelled")

# Function to show chart
def showchart():
    print("Press 1 - Books and their Cost")
    print("Press 2 - Fine Paid by Members")
    print("Press 3 - Frequently Issued Books")
    print("Press 4 - No. of Books Issued per week")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        bdf = pd.read_csv(r"C:/Users/arkan/Desktop/books.csv", encoding='latin1')
        df = bdf[["title", "cost"]]
        bdf.plot(kind='bar')
    # Add other cases as needed

# Function to show menu
def showMenu():
    print("-----------------------------")
    print("       XYZ LIBRARY MGT       ")
    print("-----------------------------")
    print("Press 1 - Add a New Book")
    print("Press 2 - Search for a Book")
    print("Press 3 - Delete a Book")
    print("Press 4 - Show All Books")
    print("Press 5 - Add a New Member")
    print("Press 6 - Search for a Member")
    print("Press 7 - Delete a Member")
    print("Press 8 - Show All Members")
    print("Press 9 - Issue a Book")
    print("Press 10 - Return a Book")
    print("Press 11 - Show All Issued Books")
    print("Press 12 - To view Charts")
    print("Press 13 - To Exit")
    choice = int(input("Enter your choice : "))
    return choice

# Main program loop
while True:
    ch = showMenu()
    if ch == 1:
        addNewBook()
    elif ch == 2:
        searchBook()
    elif ch == 3:
        deleteBook()
    elif ch == 4:
        showBooks()
    elif ch == 5:
        addNewMember()
    elif ch == 6:
        searchMember()
    elif ch == 7:
        deleteMember()
    elif ch == 8:
        showMembers()
    elif ch == 9:
        issueBook()
    elif ch == 10:
        returnBook()
    elif ch == 11:
        showIssuedBooks()
    elif ch == 12:
        showchart()
    elif ch == 13:
        break
    else:
        print("Invalid Option Selected")
