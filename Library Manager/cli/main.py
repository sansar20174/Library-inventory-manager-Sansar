import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from library_manager.book import Book
from library_manager.inventory import Inventory
from library_manager.utils import get_input

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "book.json"

def show_book(book):
    print(f"\nISBN: {book.isbn}")
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    print(f"Total Copies: {book.total_copies}")
    print(f"Issued Copies: {book.issued_copies}")
    print(f"Available: {book.available_copies}")
    print("-" * 30)

def main():
    inv = Inventory(str(DATA_FILE))

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search")
        print("6. Exit")

        choice = get_input("Choose (1-6): ")

        if choice == "1":
            isbn = get_input("ISBN: ")
            title = get_input("Title: ")
            author = get_input("Author: ")
            copies = int(get_input("Total copies: "))
            book = Book(isbn, title, author, copies)
            inv.add_book(book)
            print("Book added.")

        elif choice == "2":
            isbn = get_input("ISBN to issue: ")
            try:
                inv.issue_book(isbn)
                print("Book issued.")
            except Exception as e:
                print(e)

        elif choice == "3":
            isbn = get_input("ISBN to return: ")
            try:
                inv.return_book(isbn)
                print("Book returned.")
            except Exception as e:
                print(e)

        elif choice == "4":
            books = inv.list_all_books()
            for b in books:
                show_book(b)

        elif choice == "5":
            q = get_input("Search: ")
            results = inv.search_by_title(q)
            for b in results:
                show_book(b)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
if __name__ == "__main__":  
    main()  