import os

class Book:
    def __init__(self, title, author):
        self.title = title.strip()
        self.author = author.strip()
        self.is_borrowed = False

    def __str__(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"{self.title} by {self.author} ({status})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"\nBook '{book.title}' added successfully!")

    def show_books(self):
        if not self.books:
            print("\nNo books in the library.")
        else:
            print("\n--- Library Books ---")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                print(f"\nYou borrowed '{book.title}'.")
                return
        print(f"\nSorry, '{title}' is not available or already borrowed.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_borrowed:
                book.is_borrowed = False
                print(f"\nYou returned '{book.title}'.")
                return
        print(f"\nNo record of '{title}' being borrowed.")


# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    library = Library()

    while True:
        clear_screen()
        print("=== Library Management System ===")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            clear_screen()
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            if title and author:
                library.add_book(Book(title, author))
            else:
                print("\nInvalid input! Title and author cannot be empty.")
            input("\nPress Enter to continue...")

        elif choice == "2":
            clear_screen()
            library.show_books()
            input("\nPress Enter to continue...")

        elif choice == "3":
            clear_screen()
            if not library.books:
                print("\nNo books available to borrow.")
            else:
                title = input("Enter the book title to borrow: ").strip()
                library.borrow_book(title)
            input("\nPress Enter to continue...")

        elif choice == "4":
            clear_screen()
            if not library.books:
                print("\nNo books in the library yet.")
            else:
                title = input("Enter the book title to return: ").strip()
                library.return_book(title)
            input("\nPress Enter to continue...")

        elif choice == "5":
            clear_screen()
            print("Exiting the library system. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")
            input("\nPress Enter to try again...")


if __name__ == "__main__":
    main()
