print("""+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

Welcome To Our Library

Options;

1. See Books

2. Search Book

3. Add Book

4. Delete Book 

'q' For Exit

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n""")

library = Library()

while True:
    option = input("Option :")

    if (option == "q"):
        print("We hope to see you again.....")
        break
    elif (option == "1"):
        library.books()

    elif (option == "2"):
        name = input("Which book are you looking for?")

        library.search_book(name)

    elif (option == "3"):
        name = input("Name:")
        author = input("Author:")
        publisher = input("Publisher:")
        genre = input("Genre:")
        page = int(input("Page"))

        new_book = Book(name,author,publisher,genre,page)

        library.add_book(new_book)
        print("Book was added!!!\n",)


    elif (option == "4"):
        name = input("Which book do you want do delete?")

        library.del_book(name)
        print("Book was deleted!!!\n")
