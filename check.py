from datetime import date, timedelta  # Import for date handling

class Checkout:
  def __init__(self, book, user, checkout_date, due_date=None):
    self.book = book  # Reference to the Book object
    self.user = user  # Reference to the User object
    self.checkout_date = checkout_date  # Date the book was checked out
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
    print(f"Book: {self.book.title}")
    print(f"Borrowed by: {self.user.name}")
    print(f"Checkout Date: {self.checkout_date}")
    print(f"Due Date: {self.due_date}")
    print(f"Overdue: {'Yes' if self.is_overdue() else 'No'}")

class Library:
  # ... (existing Library class code from library.py)

  def checkout_item(self, title, user_id):
    """
    Checks out a book if available and updates checkout information.

    Args:
        title (str): Title of the book to check out.
        user_id (str): User ID of the user checking out the book.

    Returns:
        None
    """
    for item in self.items:
      if item.title == title and item.available:
        user = self.find_user(user_id)  # Find user based on ID (implement in library.py)
        if user:
          checkout = Checkout(item, user, date.today())
          item.available = False  # Update book availability
          self.checkouts.append(checkout)
          print(f"Book '{title}' checked out to {user.name}.")
          return
        else:
          print(f"User with ID '{user_id}' not found.")
      else:
        print(f"Book '{title}' is not available.")
    print("Checkout failed.")

  def checkin_item(self, title):
    """
    Checks in a book, updates availability, and removes checkout information.

    Args:
        title (str): Title of the book to check in.

    Returns:
        None
    """
    for checkout in self.checkouts:
      if checkout.book.title == title:
        checkout.book.available = True  # Update book availability
        self.checkouts.remove(checkout)
        print(f"Book '{title}' checked in.")
        return
    print(f"Book '{title}' not found in checkout records.")

  def to_dict(self):
    """
    Converts checkout information into a dictionary.

    Returns:
        dict: Dictionary containing checkout information (item data, user ID, checkout date).
    """
    return {
      "item": self.item.to_dict(),  # Assuming item has a to_dict method
      "user_id": self.user.id,  # Assuming user has an id attribute
      "checkout_date": self.checkout_date.strftime("%Y-%m-%d")  # Format date for JSON
    }

  # ... (other methods from library.py)
