import sqlite3

#first we create a Book class.
class Book():

    def __init__(self,name,author,publisher,genre,page):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.page = page

    def __str__(self):
        return "Book: {}\nAuthor: {}\nPublisher: {}\nGenre: {}\nPage: {}\n".format(self.name,self.author,self.publisher,self.genre,self.page)

class Library():

    def __init__(self):
        
        self.create_connect() #we want to connect sqlite database when our class is called, so we call our create_connect() method
    
    def create_connect(self):  #to connect sqlite database we create a function

        self.connect = sqlite3.connect("library.db") #create a database
        
        self.cursor = self.connect.cursor() #let's create a cursor 

        self.cursor.execute("CREATE TABLE IF NOT EXISTS books (name TEXT, author TEXT,publisher TEXT, genre TEXT, page INT)")  # create a table in our library.db

        self.connect.commit()

    def disconnect(self):
        self.connect.close()

    def books(self):

        self.cursor.execute("SELECT * FROM books")

        all_books = self.cursor.fetchall() # our books are in tuples inside a list
        # (THIS IS AN EXAMPLE OF WHAT YOU SHOULD EXPECT)
        # all_books =[('Catch 22', 'Joseph Heller', 'Simon & Schuster', 453), ('The Catcher in the Rye', 'J. D. Salinger', 'Simon & Schuster', 250), ("Harry Potter - Philosopher's Stone", 'J. K. Rowling', 'Bloomsbury', 233)]

        if len(all_books) == 0 :
            print("Library is empty!!!\n")
        else:
            for i in all_books:

                book = Book(i[0],i[1],i[2],i[3],i[4]) # We define a Book class object.
                print(book) #now we use print function. so we call __str__ method of our book object.

    def search_book(self,name):

        self.cursor.execute("SELECT * FROM books WHERE name =?",(name,))

        all_books = self.cursor.fetchall() 

        if len(all_books) == 0 :
            print("We don't have this book!!!\n")
        else:
            book = Book(all_books[0][0],all_books[0][1],all_books[0][2],all_books[0][3],all_books[0][4])

            print(book)
    
    def add_book(self,book):

        self.cursor.execute("INSERT INTO books VALUES(?,?,?,?,?)",(book.name,book.author,book.publisher,book.genre,book.page))

        self.connect.commit()

    def del_book(self,name):
        self.cursor.execute("DELETE FROM books WHERE name=?",(name,))

        self.connect.commit()
