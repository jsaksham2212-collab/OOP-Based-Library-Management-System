import json
from datetime import datetime 

#Loading Books json file
with open("books.json","r")as file1:
    book_s=json.load(file1)

#Loading Books json file
with open("users.json","r")as file2:
    user_s=json.load(file2)

#Saving data in Book json file
def save_books():
    with open("books.json","w")as file1:
        json.dump(book_s,file1,indent=4)

#Saving data in User json file
def save_users():
    with open("users.json","w")as file2:
        json.dump(user_s,file2,indent=4)



class Book:
    def __init__(self,book_id,title,author,is_borrowed="False"):
        self.book_id=book_id 
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed
        
class Fiction(Book):
    def __init__(self, book_id, title, author,category="Fiction", is_borrowed="False"):
        super().__init__(book_id, title, author, is_borrowed)
        self.category=category
class Finance(Book):
    def __init__(self, book_id, title, author,category="Finance", is_borrowed="False"):
        super().__init__(book_id, title, author, is_borrowed)
        self.category=category
class Selfhelp(Book):
    def __init__(self, book_id, title, author,category="Self Help", is_borrowed="False"):
        super().__init__(book_id, title, author, is_borrowed)
        self.category=category
class Programming(Book):
    def __init__(self, book_id, title, author,category="Programming", is_borrowed="False"):
        super().__init__(book_id, title, author, is_borrowed)
        self.category=category

class User:
    def __init__(self,User_id,Name,Book_id,date_of_Borrow,is_returned):
        self.User_id=User_id 
        self.Name=Name
        self.is_returned=is_returned
        self.Book_id=Book_id
        self.date_of_Borrow=date_of_Borrow


class library(Book,User):
    def __init__(self):
        self.books=[]
        self.users=[]       
        

    #Adding a new Book
    def add_book(self,book):
        self.books.append(book)
        book_s.append({"Book_id":book.book_id,"Title":book.title,"Author":book.author,"Category":book.category,"is_borrowed":book.is_borrowed})
        save_books()
        print("Book Added Successfully")
    

    #Viweing all the Books
    def view_books(self):
        for book in book_s:
            print(f"""
Book id : {book['Book_id']}
Title : {book['Title']}
Author : {book['Author']}
Borrowed : {book['is_borrowed']}
""")
    
    #Viewing all the Users
    def view_users(self):
        for user in self.users:
            print(f"""
User id : {self.User_id}
Name : {self.Name}
Book id : {self.Book_id}
date_of_borrow : {self.date_of_Borrow}
Returned : {self.is_returned}
""")


    #Searching the Book
    def search_book(self,title):
        for book in book_s:
            if book['Title'].lower()==title.lower():
                print(f"""
Book id : {book['Book_id']}
Title : {book['Title']}
Author : {book['Author']}
Category : {book['Category']}
Borrowed : {book['is_borrowed']}""")
        if book['Title']!=title:
            print("Not found ")


    #Borrowing the Book 
    def borrow_book(self,title):
        for book in book_s:
            if book["Title"].lower()==title.lower():
                if book["is_borrowed"]=="True":
                    print("Book Already Borrowed")
                    break
                else:
                    #Validation of Userid
                    while True:
                        user_id=input("Enter User id : ")
                        if user_id.strip()=="":
                            print("User id cannot be empty")
                        elif user_id.isdigit()==False:
                            print("User id must be a Number")
                        else:
                            break

                    #Validation of Name
                    while True:
                        name=input("Enter User Name : ")
                        if name.strip()=="":
                            print("Name cannot be empty")
                        elif name.replace(" ", "").isalpha()==False:
                            print("Name should contain only letters")
                        else:
                            break
                
                    bookid=book["Book_id"]
                    Is_returned="False"
                    borrow_date=datetime.now().strftime("%d-%m-%Y")
                    user_s.append({"User_id":user_id,"Name":name,"Book_id":bookid,"date_of Borrow":borrow_date,"is_returned":Is_returned,})
                    save_users()
                    book["is_borrowed"]="True"
                    print("Book Borrowed Successfully")
                    save_books()

                        
    #Returning the Book 
    def return_book(self,title):
        for book in book_s:
            if book["Title"].lower()==title.lower():
                if book["is_borrowed"]=="False":
                    print("Book was Not Borrowed")
                else:
                    bookid=book["Book_id"]
                    for user in user_s:
                        if user["Book_id"]==bookid:
                            user["is_returned"]="True"
                            save_users()
                    book["is_borrowed"]="False"
                    print("Book Returned Successfully")
                    save_books()

                    

library = library()

# while True:

#     print("""
# ===== LIBRARY MENU =====

# 1. Add Book
# 2. View Books
# 3. Search Book
# 4. Borrow Book
# 5. Return Book
# 6. Exit
# """)

#     choice = input("Enter Choice: ")

#     if choice == "1":
#         #Validation of Bookid
#         while True:
#             book_id = input("Enter Book ID: ")
#             duplicate=False
#             for book in book_s:
#                 if book["Book_id"]==book_id:
#                     duplicate=True
#             if duplicate==True:
#                 print("Book id already exist")
#             elif book_id.strip()=="":
#                 print("Book id cannot be empty")
#             elif book_id.isdigit()==False:
#                 print("Book id must be a Number")
#             else:
#                 break

#         #Validation of Title
#         while True:
#             title = input("Enter Title: ")
#             if title.strip()=="":
#                 print("Title cannot be empty")
#             elif title.replace(" ", "").isalpha()==False:
#                 print("Title should contain only letters")
#             else:
#                 break
        
#         #Validation of Author Name
#         while True:
#             author = input("Enter Author: ")
#             if author.strip()=="":
#                 print("Author Name cannot be empty")
#             elif author.replace(" ", "").isalpha()==False:
#                 print("Author Name should contain only letters")
#             else:
#                 break

#         category=input("Enter Category: ")
#         if category.lower()=="fiction":
#             book = Fiction(book_id, title, author)
#             library.add_book(book)
#             break
#         elif category.lower()=="finance":
#             book = Finance(book_id, title, author)
#             library.add_book(book)
#             break
#         elif category.lower()=="self help":
#             book = Selfhelp(book_id, title, author)
#             library.add_book(book)
#             break
#         elif category.lower()=="programming":
#             book = Programming(book_id, title, author)
#             library.add_book(book)
#             break
#         else:
#             print("Invalid Category")
#             break

#     elif choice == "2":
#         library.view_books()

#     elif choice == "3":

#         title = input("Enter Title To Search: ")

#         library.search_book(title)


#     elif choice == "4":

#         title = input("Enter Book Title: ")

#         library.borrow_book(title)

#     elif choice == "5":

#         title = input("Enter Book Title: ")

#         library.return_book(title)

#     elif choice == "6":

#         print("Thank You")

#         break

#     else:
#         print("Invalid Choice")
        
library.view_users(User)