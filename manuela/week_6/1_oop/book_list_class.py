from book_class import Book 

class Booklist():
	# Initialization function
	def __init__(self):
		# initialize books attribute
		self.books = []
		
	# method to add a book
	def add(self, title, author):
		book = Book(title, author)
		# append to books attribute (the list)
		self.books.append(book)

	# method to count the books by taking length of books attribute
	def count_books(self):
		return len(self.books)

	# method to remove a book by title
	def remove_title(self, title):
		# loop throubh books, remove the book if the title matches title passed in
		for book in self.books:
			if book.title == title:
				self.books.remove(book)
	
	def display_titles(self):
		print(sorted([book.title for book in self.books]))

	def is_empty(self):
		"""Return True if the book list is empty, False if not"""
		return len(self.books) == 0

# nyt_bestsellers = []
# for book in nyt_bestsellers:
# 	nyt_bestsellers.append(book.title)
#     #nyt_bestsellers.append(book.title)
# # 	# method to display all book titles in alphabetical order
	
# 		# loop through books attribute and add all titles to list
# for book in Booklist:
# 	book.append(book.title)
# 		# sort titles alphabetically

		
# 		# print sorted titles
# 		print(titles)
		