'''
Book Class

You create a class that represents a single book.
The goal is to practise how objects hold data and how they behave through methods.

What the class must store

Each book needs:
	•	a title
	•	an author
	•	a year of release
	•	a rating

These become the attributes of the object.

What the class must do
	1.	Give a short summary
Create a method that returns a brief line with the book title, the author, and the year.
This is to show how an object can describe itself.
	2.	Update the rating with simple rules
Create a method that receives a new rating.
The method accepts the update only when the value is between one and five.
This teaches you how to protect the internal state of an object.
	3.	Filter books in a list
After you create several book objects and store them in a list,
write a separate function idea that returns only the books released after the year two thousand.
This is to practise how objects behave inside collections.
'''

class Book():
    def __init__(self, title, author, year, rating):
        self.title = title
        self.author = author
        self.year = year
        self.rating = rating

    def print_book(self):
        print(
        f'Title: {self.title.title()}\n' \
        f'Author: {self.author.title()}\n'\
        f'Year: {self.year}\n'\
        f'Rating: {self.rating}'
        )

    def book_rating(self):
        user_rating = int(input('How would you rate this book? (by 1 ro 5)\n'))
        rating = "*" * user_rating
        return rating
    
    def ins_book(self):
        print('Insert a new book to your reading list.')
        b_title = input('Enter book title:\n').lower()
        b_author = input('Enter the author name:\n').lower()
        b_year = input('Enter the year when the book has been pubblished:\n')
        b_rat = book.book_rating(self)
        print(f'Horay! {b_title} by {b_author} has been added to your reading list! ')
                         


user_rat = book.book_rating()
book = Book("100 years of solitude", "gabriel garcia marquez", 1930, user_rat)
book.print_book()