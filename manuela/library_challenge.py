'''
print('Question 1:')
# You are working on a library management system, here are the list books at the library
books = ['MY OWN WORDS', 'WHITE FRAGILITY', 'THE BODY KEEPS THE SCORE', 'SO YOU WANT TO TALK ABOUT RACE', 'STAMPED FROM THE BEGINNING', 'JUST MERCY', 'BORN A CRIME',
         'THE WARMTH OF OTHER SUNS', 'THE COLOR OF LAW', 'THE NEW JIM CROW', 'THE TRUTHS WE HOLD', 'SAPIENS', 'BRAIDING SWEETGRASS', "MY GRANDMOTHER'S HANDS", 'ON TYRANNY']

# 1.0
# What data type is the object 'books'? How do you know?
print(type(books))  #expect list

# 1.1
# Create a function 'available_books' to print the books list
# Parameters: Not needed for this function
# Return: Not needed for this function
def available_books():
    print(books)
# 1.2
# Run the 'available_books' function
available_books()
print()


# 1.3
# Create a function 'check_out' that removes a book from the books list
# Parameters: book (string)
# Return: Not needed for this function
def check_out(book):
    books.remove(book)   #remove a book
# 1.4
# Check out 'SAPIENS' using the check_out function
check_out('SAPIENS')      #checking out 'SAPIENS' in particular
# Bonus: Run available_books function again to see if the book was checked out
available_books()           #calling the function
print('SAPIENS' in books)   #checking if book was removed

# 1.5
# Create a function 'check_in' that adds a book to the books list
# Parameters: book (string)
# Return: Not needed for this function
def check_in(book):
    books.append(book)    #added any book


# 1.6
# Check in 'SAPIENS' using the check_in function
check_in('SAPIENS')
# Bonus: Run available_books function to see if the book was checked in
available_books()           #run (call) the function
print('SAPIENS' in books)   #checking if "SAPIENS" was added
# 1.7
# Create a function 'search_by_name' that prints 'Available' if exists in books list, 'Not Available' if it doesn't.
# Parameters: book (string)
# Return: Not needed for this function
def search_by_name(book):
    if book in books:          #if statement for the books list
        print("Available")   #if there print this
    else:
        print("Not Available")   #if not (else) print this
search_by_name('JUST MERCY')    
# 1.8
# Search for the book 'JUST MERCY'

print()
'''
from doctest import OutputChecker


print('Question 2')
# Here's the same list of books, with additional details
books_with_details = [
    {
        'title': 'MY OWN WORDS',
        'author': 'Ruth Bader Ginsburg with Mary Hartnett and Wendy W Williams',
        'description': 'A collection of articles and speeches by the Supreme Court justice.'
    },
    {
        'title': 'WHITE FRAGILITY',
        'author': 'Robin DiAngelo',
        'description': 'Historical and cultural analyses on what causes defensive moves by white people and how this inhibits cross-racial dialogue.'
    },
    {
        'title': 'THE BODY KEEPS THE SCORE',
        'author': 'Bessel van der Kolk',
        'description': 'How trauma affects the body and mind, and innovative treatments for recovery.'
    },
    {
        'title': 'SO YOU WANT TO TALK ABOUT RACE',
        'author': 'Ijeoma Oluo',
        'description': 'A look at the contemporary racial landscape of the United States.'
    },
    {
        'title': 'STAMPED FROM THE BEGINNING',
        'author': 'Ibram X Kendi',
        'description': 'Winner of the 2016 National Book Award for nonfiction. A look at anti-Black racist ideas and their effect on the course of American history.'
    },
    {
        'title': 'JUST MERCY',
        'author': 'Bryan Stevenson',
        'description': 'A civil rights lawyer and MacArthur grant recipient’s memoir of his decades of work to free innocent people condemned to death.'
    },
    {
        'title': 'BORN A CRIME',
        'author': 'Trevor Noah',
        'description': 'A memoir about growing up biracial in apartheid South Africa by the host of “The Daily Show.”'
    },
    {
        'title': 'THE WARMTH OF OTHER SUNS',
        'author': 'Isabel Wilkerson',
        'description': 'An account of the Great Migration of 1915-70, in which six million African-Americans abandoned the South.'
    },
    {
        'title': 'THE COLOR OF LAW',
        'author': 'Richard Rothstein',
        'description': 'A case for how the American government abetted racial segregation in metropolitan areas across the country.'
    },
    {
        'title': 'THE NEW JIM CROW',
        'author': 'Michelle Alexander',
        'description': 'A law professor on the “war on drugs” and its role in the disproportionate incarceration of Black men.'
    },
    {
        'title': 'THE TRUTHS WE HOLD',
        'author': 'Kamala Harris',
        'description': 'A memoir by the daughter of immigrants who is now a California senator and the 2020 Democratic candidate for vice president.'
    },
    {
        'title': 'SAPIENS',
        'author': 'Yuval Noah Harari',
        'description': 'How Homo sapiens became Earth’s dominant species.'
    },
    {
        'title': 'BRAIDING SWEETGRASS',
        'author': 'Robin Wall Kimmerer',
        'description': 'A botanist and member of the Citizen Potawatomi Nation espouses having an understanding and appreciation of plants and animals.'
    },
    {
        'title': 'MY GRANDMOTHER\'S HANDS',
        'author': 'Resmaa Menakem',
        'description': 'A therapist who specializes in trauma, body-centered psychotherapy and violence prevention explains racism\'s effect on the body.'
    },
    {
        'title': 'ON TYRANNY',
        'author': 'Timothy Snyder',
        'description': 'Twenty lessons from the 20th century about the course of tyranny.'
    },
    {
        'title': 'THE ROAD TO UNFREEDOM',
        'author': 'Timothy Snyder',
        'description': 'Snyder explores Russian attempts to influence Western democracies and the influence of philosopher Ivan Ilyin on Russian President Vladimir Putin and the Russian Federation in general.'
    }
]

# 2.0
# Describe the structure of the data in books_with_details. What types of data are nested within others? How do you know? 
# This is a list of dictionaries with strings as key value as types
# This is a list(defined by []) with multiple dictionaries contained within.
#How do you know? by the separators
print(type(books_with_details))  
print(type(books_with_details [0]))
print(type(books_with_details [0]['title']))


# 2.1
# Create a function 'count_books' that returns the number of books in the books_with_details list
# Parameters: Not needed for this function
# Return: number of books (integer)
#count_books()
 # Return: number of books (integer)   
def count_books():       
    print((len(books_with_details)))
count_books()
print()

# 2.2
# Check the number of books available in the books list using the count_books function
print(type(len('books_with_details')))
print()

# 2.3
# Create a function 'search_by_author' that returns the titles of books by an author
# Parameters - author (string)
# Return - author's books (list of strings)
# Hint - You will need a for loop, if statement, .append() for this solution!
i = 'author'
#def search_by_author():
for i in books_with_details:
        if i in books_with_details[1]:
            print('author')
    #author.append('author')
    
       
        #print(books_with_details in range()['author'])
   # if author in books_with_details:
#search_by_author()
#print(authors_books[1:])
       # if i in authors_books():

    

#search_by_author()
'''
    for a in author:
        if author_in_list
    print(books_with_details [1]['author'])
search_by_author()

# 2.4
# Search for book titles by the author 'Timothy Snyder' using the search_by_author function

'''