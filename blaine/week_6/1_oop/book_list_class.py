from book_class import Book


class Booklist():
    def __init__(self):
        """Initialize the empty book list"""
        self.books = []

    def add(self, title, author):
        """Add a Book object with the given title and author to the book list"""
        book = Book(title, author)
        self.books.append(book)

    def count_books(self):
        """Return the number of books currently in the booklist"""
        return len(self.books)

    def remove_title(self, title):
        """Remove a book from the book list"""
        self.books = [
            book for book in self.books if book.title.lower() != title.lower()]

    def display_titles(self):
        """Print out all titles currently in the book list"""
        sorted_books = sorted(
            self.books, key=lambda book: book.title)
        alpha_books = [book.title for book in sorted_books]
        print(alpha_books)

    def is_empty(self):
        """Return True if the book list is empty, False if not"""
        if self.books:
            return False
        return True
