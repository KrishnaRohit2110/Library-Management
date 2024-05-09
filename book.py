class Book:
  def __init__(self, title, author, isbn, available=True):
    self.title = title
    self.author = author
    self.isbn = isbn
    self.available = available

  def display_info(self):
    print(f"Title: {self.title}")
    print(f"Author: {self.author}")
    print(f"ISBN: {self.isbn}")
    print(f"Available: {self.available}")
