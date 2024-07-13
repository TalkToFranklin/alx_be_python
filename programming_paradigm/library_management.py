class Book:
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        _is_checked_out (bool): Indicates whether the book is currently checked out.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        # Checks out the book, marking it as unavailable.
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        #  Returns the book, marking it as available.
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        # Returns True if the book is available, False otherwise.
        return not self._is_checked_out

class Library:
    """
    Represents a library that manages a collection of books.

    Attributes:
        _books (list): The list of books in the library.
    """
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
    """
    Adds a book to the library.
        Args/Input:
            book (Book): The book to be added.
        """

    def check_out_book(self, title):
        """
        Checks out a book from the library.

        Args:
            title (str): The title of the book to be checked out.

        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"'{title}' not found in the library.")
    """ Another simpler rendition of the logic in the code above is
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False
    """
    
    def return_book(self, title):
        """
        Returns a book to the library.

        Args:
            title (str): The title of the book to be returned.

        Returns:
            bool: True if the book was successfully returned, False otherwise.
        """
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        # Prints a list of all available books in the library.
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        
        """ 
        Alternative logic for code block above
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
        
        """



"""
How Tos / Explanation
library_management.py
1. Book Class:

    Attributes:
        title: Title of the book.
        author: Author of the book.
        _is_checked_out: A private attribute to track if the book is checked out.
    Methods:
        check_out(): Marks the book as checked out if it is not already checked out.
        return_book(): Marks the book as returned if it is currently checked out.
        is_available(): Returns True if the book is available, otherwise False.
2. Library Class:

    Attributes:
        _books: A private list to store instances of Book.
    Methods:
        add_book(book): Adds a book to the library's collection.
        check_out_book(title): Checks out a book by its title if available.
        return_book(title): Returns a book by its title if it was checked out.
        list_available_books(): Lists all available books in the library.

main.py
1. Setup a Library: Adds two books to the library.
2. List Available Books: Displays the list of available books.
3. Check Out a Book: Simulates checking out a book and updates the available books list.
4. Return a Book: Simulates returning a book and updates the available books list.

By following the given instructions, this implementation ensures that the Book and Library classes function correctly, and the main.py script demonstrates the functionality through a simple interface.


Don't be perplexed broken down explanation:
1. The Book class represents a book in the library. It has two public attributes, title and author, and a private attribute _is_checked_out to track the availability of the book.
2. The Book class provides methods to check out a book (check_out), return a book (return_book), and check if a book is available (is_available).
3. The Library class manages a collection of books. It has a private list _books to store the Book instances.
4. The Library class provides methods to add a book (add_book), check out a book (check_out_book), return a book (return_book), and list all available books (list_available_books).
5. The check_out_book method searches for the book with the given title in the _books list, and if the book is available, it marks it as checked out.
6. The return_book method searches for the book with the given title in the _books list, and if the book is checked out, it marks it as available.
7. The list_available_books method prints the title and author of all available books in the _books list.
To use these classes, you can create a main.py script as provided.
"""