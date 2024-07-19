class Book:
    def __init__(self, title: str, author: str, year: int):
        #Initialize a Book instance with title, author, and year.
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        #Destructor that prints a message when the object is deleted.
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a string representation of the Book instance 
        in the format '(title) by (author), published in (year)"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        #Return an official string representation of the Book instance.
        return f"Book('{self.title}', '{self.author}', {self.year})"