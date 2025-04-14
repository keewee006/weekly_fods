'''Basic Library Management using OOP and File Handling'''
import json

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued = False

class Library:
    def __init__(self, filename='library.json'):
        self.filename = filename
        try:
            with open(filename, 'r') as f:
                self.books = json.load(f)
        except:
            self.books = []

    def save_books(self):
        with open(self.filename, 'w') as f:
            json.dump(self.books, f)

    def add_book(self, title, author):
        self.books.append({'title': title, 'author': author, 'issued': False})
        self.save_books()

    def issue_book(self, title):
        for book in self.books:
            if book['title'] == title and not book['issued']:
                book['issued'] = True
                self.save_books()
                print(f"{title} issued.")
                return
        print("Book not available.")

    def return_book(self, title):
        for book in self.books:
            if book['title'] == title and book['issued']:
                book['issued'] = False
                self.save_books()
                print(f"{title} returned.")
                return
        print("Book not found or not issued.")

    def search_book(self, title):
        found = [b for b in self.books if title.lower() in b['title'].lower()]
        for b in found:
            print(f"{b['title']} by {b['author']} - {'Issued' if b['issued'] else 'Available'}")
        if not found:
            print("No books found.")

# Example usage
lib = Library()
lib.add_book("Harry Potter", "J.K. Rowling")
lib.issue_book("Harry Potter")
lib.search_book("Harry")
lib.return_book("Harry Potter")
