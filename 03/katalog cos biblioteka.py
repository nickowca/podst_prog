class Book:
    def __init__(self, author, title, category, pages, year):
        self.author = author
        self.title = title
        self.category = category
        self.pages = pages
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - {self.category}, {self.pages} pages"

class Library:
    book_count = 0
    def __init__(self):
        self.books = []

    def _if_exists(self, book_title) -> bool:
        return any(book.title == book_title for book in self.books)

    def add_book(self, new_book: Book):
        if self._if_exists(new_book.title):
            print("Book already exists in the library.")
            return
        else:
            self.books.append(new_book)
            Library.book_count += 1

    def show_books(self):
        for book in self.books:
            print(book)

    def delete_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                Library.book_count -= 1
                break

    def save_file(self, filename):
        try:
            with open(filename, 'w') as file:
                for book in self.books:
                    file.write(f"{book.author};{book.title};{book.category};{book.pages};{book.year}\n")
        except Exception as e:
            print(f"An error occurred while saving: {e}")

    def import_books(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    author, title, category, pages, year = line.strip().split(';')
                    self.add_book(Book(author, title, category, int(pages), int(year)))
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")





def menu(library: Library):
    while True:
        print("\nMenu:")
        print("1. Add book")
        print("2. Show books")
        print("3. Remove book (by title)")
        print("4. Show book count")
        print("5. Import books from file")
        print("6. Save books to file")
        print("7. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            author = input("Author: ").strip()
            title = input("Title: ").strip()
            category = input("Category: ").strip()
            pages = input("Number of pages: ").strip()
            try:
                pages = int(pages)
            except ValueError:
                print("Invalid number of pages, set to 0.")
                pages = 0
            year = input("Year of publication: ").strip()
            try:
                year = int(year)
            except ValueError:
                print("Invalid year, set to 0.")
                year = 0
            new_book = Book(author, title, category, pages, year)
            library.add_book(new_book)

        elif choice == "2":
            if not library.books:
                print("No books in the library.")
            else:
                library.show_books()

        elif choice == "3":
            title = input("Enter title to remove: ").strip()
            library.delete_book(title)

        elif choice == "4":
            print("Number of books:", Library.book_count)

        elif choice == "5":
            filename = input("Enter filename to import from: ").strip()
            library.import_books(filename)

        elif choice == "6":
            filename = input("Enter filename to save to: ").strip()
            library.save_file(filename)

        elif choice == "7":
            print("Program terminated.")
            break

        else:
            print("Invalid choice. Select 1-7.")


l = Library()
l.add_book(Book("J.K. Rowling", "Harry Potter and the Sorcerer's Stone", "Fantasy", 309, 1997))
menu(l)






