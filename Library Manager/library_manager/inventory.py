import json
from pathlib import Path
from library_manager.book import Book

class Inventory:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.books = self.load_inventory()

    def load_inventory(self):
        if not self.file_path.exists():
            return {}
        with open(self.file_path, 'r') as f:
            data = json.load(f)
            books = {book_data['isbn']: Book(**book_data) for book_data in data}
            return books

    def save_inventory(self):
        with open(self.file_path, 'w') as f:
            data = [book.__dict__ for book in self.books.values()]
            json.dump(data, f, indent=4)

    def add_book(self, book: Book):
        if book.isbn in self.books:
            existing_book = self.books[book.isbn]
            existing_book.total_copies += book.total_copies
        else:
            self.books[book.isbn] = book
        self.save_inventory()

    def issue_book(self, isbn: str):
        if isbn not in self.books:
            raise ValueError("Book with given ISBN does not exist in inventory.")
        book = self.books[isbn]
        book.issue_copy()
        self.save_inventory()

    def return_book(self, isbn: str):
        if isbn not in self.books:
            raise ValueError("Book with given ISBN does not exist in inventory.")
        book = self.books[isbn]
        book.return_copy()
        self.save_inventory()

    def list_all_books(self):
        return list(self.books.values())
    
    def search_by_title(self, text):
        return [book for book in self.books.values()
                 if text.lower() in book.title.lower()]