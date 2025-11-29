class Book:
    def __init__(self, isbn, title, author, total_copies, issued_copies=0):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.issued_copies = issued_copies

    @property
    def available_copies(self):
        return self.total_copies - self.issued_copies

    def issue_copy(self):
        if self.available_copies <= 0:
            raise ValueError("No available copies to issue.")
        self.issued_copies += 1

    def return_copy(self):
        if self.issued_copies <= 0:
            raise ValueError("No issued copies to return.")
        self.issued_copies -= 1