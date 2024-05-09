from datetime import date, timedelta  # Import for date handling

class Item:
  def __init__(self, title, available=True):
    self.title = title
    self.available = available

  def display_info(self):
    print(f"Title: {self.title}")
    print(f"Available: {self.available}")

  def to_dict(self):
    return {
      "title": self.title,
      "available": self.available
    }

class Book(Item):
  def __init__(self, title, author, isbn, available=True):
    super().__init__(title, available)  # Inherit from Item class
    self.author = author
    self.isbn = isbn

class User:
  def __init__(self, name, user_id):
    self.name = name
    self.user_id = user_id

  def display_info(self):
    print(f"Name: {self.name}")
    print(f"User ID: {self.user_id}")

  def to_dict(self):
    return {
      "name": self.name,
      "user_id": self.user_id
    }

# (Optional) Base class for different checkout types
class CheckoutBase:
  def __init__(self, item, user, checkout_date):
    self.item = item
    self.user = user
    self.checkout_date = checkout_date

class Checkout(CheckoutBase):  # Example checkout class inheriting from CheckoutBase
  def __init__(self, book, user, checkout_date, due_date=None):
    super().__init__(book, user, checkout_date)  # Inherit from CheckoutBase
    self.due_date = due_date if due_date else self.calculate_due_date()  # Calculate due date if not provided

  def calculate_due_date(self, loan_period=14):  # Example loan period of 14 days
    """
    Calculates the due date for a checkout based on a loan period (in days).

    Args:
        loan_period (int, optional): Loan period in days. Defaults to 14.

    Returns:
        date: Due date for the checkout.
    """
    return self.checkout_date + timedelta(days=loan_period)

  def is_overdue(self):
    """
    Checks if the current date is past the due date of the checkout.

    Returns:
        bool: True if overdue, False otherwise.
    """
    return self.due_date < date.today()

  def display_info(self):
    print(f"Book: {self.item.title}")  # Access title through item object
    print(f"Borrowed by: {self.user.name}")
    print(f"Checkout Date: {self.checkout_date}")
    print(f"Due Date: {self.due_date}")
    print(f"Overdue: {'Yes' if self.is_overdue() else 'No'}")
