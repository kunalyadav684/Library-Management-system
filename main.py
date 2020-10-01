class Library:

    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lendDict = {}

    def display_book(self, book):
        print(f"We have following books : {self.name}")
        for book in self.bookslist:
            print(book)

    def lend_book(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("You can take the book Now.")
        else:
            print(f"Sorry the book has already been taken by {self.lendDict[book]}")

    def add_book(self, book):
        self.bookslist.append(book)
        print("The book has been added to the system.")

    def return_book(self, book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    harry = Library(['Python', 'Java', 'c++', 'c'], "KK Foundation")

    while True:
        print("Welcome to the KK Foundation Library. Choose the operation you want to choose")
        user_choice = int(input("1.Display Book \n"
                                "2.Lend Book \n"
                                "3.Add Book \n"
                                "4.Return Book \n"))
        if user_choice == 1:
            harry.display_book(Library)
        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name")
            harry.lend_book(user, book)
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add: ")
            harry.add_book(book)
        elif user_choice == 4:
            book = input("Enter the name of the book you want to return: ")
            harry.return_book(book)
        else:
            print("Incorrect Choice")

        user_choice2 = input("What you want to do now? Press c to continue and q to exit")
        if user_choice2 == 'q':
            exit()
        elif user_choice2 == "c":
            continue
        else:
            print('Incorrect Choice')
