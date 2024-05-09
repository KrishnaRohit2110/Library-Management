from models import Item, Book, User, Checkout
import storage  # Import for data persistence
from datetime import date

class Library:
  def __init__(self):
    self.filename = "library_data.json"
    self.data = storage.load_data(self.filename)
    self.items = []  # Changed to handle potential future item types (e.g., Audiobook)
    for item_data in self.data.get("items", []):  # Handle potential missing "items" key
      self.items.append(Book(**item_data))  # Use unpacking for item creation
    self.users = [User(**user_data) for user_data in self.data.get("users", [])]  # Similar for users
    self.checkouts = [Checkout(**checkout_data) for checkout_data in self.data.get("checkouts", [])]

  def add_item(self, item):  # Polymorphic method for adding items (Book or future types)
    """
    Adds a new item (Book or potentially other subclasses of Item) to the library.

    Args:
        item: An object of a class inheriting from Item (e.g., Book).

    Returns:
        None
    """
    if isinstance(item, Item):  # Check if item is a subclass of Item
      self.items.append(item)
      print("Item added.")
    else:
      print("Invalid item type, please add a Book object or an object inheriting from Item.")

  def update_item(self, title, new_data=None):  # Can be modified to handle different item types
    """
    Updates an existing item (currently only Book) based on title.

    Args:
        title (str): Title of the item to update.
        new_data (dict): Dictionary containing new data for the item (e.g., author, isbn).

    Returns:
        None
    """
    for item in self.items:
      if item.title == title:
        # Update attributes based on new_data (consider validation for specific attributes)
        for key, value in new_data.items():
          setattr(item, key, value)  # Dynamic attribute update
        print(f"Item '{title}' updated.")
        return
    print(f"Item '{title}' not found.")

  def delete_item(self, title):
    """
    Deletes an existing item (currently only Book) based on title.

    Args:
        title (str): Title of the item to delete.

    Returns:
        None
    """
    for i, item in enumerate(self.items):
      if item.title == title:
        del self.items[i]
        print(f"Item '{title}' deleted.")
        return
    print(f"Item '{title}' not found.")

  def list_items(self):
    """
    Prints information about all items (currently only Books) in the library.
    """
    if not self.items:
      print("No items in the library.")
      return
    print("** Available Items **")
    for book, item in enumerate(self.items):
      print("Book ",book+1,"\n------------")
      print("Title: ", item.title)
      print("Author: ", item.author)
      print("ISBN: ", item.isbn)
      print("availability: ", item.available,"\n\n")
    #   call display_info specific to the item type (Book)

  def search_items(self, title=None, author=None, isbn=None):
    """
    Searches for items (currently only Books) based on optional title, author, or ISBN.

    Args:
        title (str, optional): Title to search for. Defaults to None.
        author (str, optional): Author to search for. Defaults to None.
        isbn (str, optional): ISBN to search for. Defaults to None.

    Returns:
        None
    """
    matches = []
    for item in self.items:
      if (title.lower() == item.title.lower()):
         matches.append(item)
         continue
      elif (author.lower() == item.author.lower()):
        matches.append(item)
        continue
      elif (isbn == item.isbn):
        matches.append(item)
        continue
    if matches:
      print("** Search Results **")
      for item in matches:
        item.display_info()
    else:
      print("No items found matching your search criteria.")

  def add_user(self, name, user_id):
    """
    Adds a new user to the library system.

    Args:
        name (str): Name of the user.
        user_id (str): Unique identifier for the user.

    Returns:
        None
    """
    if not self.find_user(user_id):  # Check for duplicate user ID
      self.users.append(User(name, user_id))
      print(f"User '{name}' (ID: {user_id}) added successfully.")
    else:
      print(f"Error: User ID '{user_id}' already exists.")

  def update_user(self, user_id, new_name=None):
    """
    Updates user information based on user ID.

    Args:
        user_id (str): User ID of the user to update.
        new_name (str, optional): New name for the user (optional). Defaults to None.

    Returns:
        None
    """
    user = self.find_user(user_id)
    if user:
      if new_name:
        user.name = new_name
      print(f"User '{user_id}' information updated successfully.")
    else:
      print(f"Error: User with ID '{user_id}' not found.")

  def delete_user(self, user_id):
    """
    Deletes a user from the library system.

    Args:
        user_id (str): User ID of the user to delete.

    Returns:
        None
    """
    user_index = self.find_user_index(user_id)
    if user_index != -1:  # Check if user exists
      del self.users[user_index]
      # Remove checkouts associated with the user (optional)
      self.checkouts = [checkout for checkout in self.checkouts if checkout.user.user_id != user_id]
      print(f"User '{user_id}' deleted successfully.")
    else:
      print(f"Error: User with ID '{user_id}' not found.")

  def find_user(self, user_id):
    """
    Finds a user object based on user ID.

    Args:
        user_id (str): User ID to search for.

    Returns:
        User: User object if found, None otherwise.
    """
    for user in self.users:
      if user.user_id == user_id:
        return user
    return None

  def find_user_index(self, user_id):
    """
    Finds the index of a user in the users list based on user ID.

    Args:
        user_id (str): User ID to search for.

    Returns:
        int: Index of the user in the list if found, -1 otherwise.
    """
    for i, user in enumerate(self.users):
      if user.user_id == user_id:
        return i
    return -1

  def checkout_item(self, title, user_id):
    """
    Checks out a book to a user.

    Args:
        title (str): Title of the book to checkout.
        user_id (str): User ID of the user checking out the book.

    Returns:
        None
    """
    book = self.find_item(title)  # Find the book object based on title
    user = self.find_user(user_id)  # Find the user object based on ID
    if book and book.available and user:  # Check if book is available and user exists
        book.available = False  # Mark book as unavailable
        self.checkouts.append(Checkout(book, user, date.today()))  # Create a checkout record
        print(f"Book '{title}' successfully checked out to user '{user.name}' (ID: {user_id}).")
    else:
        if not book:
            print(f"Error: Book '{title}' not found.")
        elif not book.available:
            print(f"Error: Book '{title}' is currently unavailable.")
        elif not user:
            print(f"Error: User with ID '{user_id}' not found.")

  def checkin_item(self, title):
    """
    Checks in a book, making it available again.

    Args:
        title (str): Title of the book to check in.

    Returns:
        None
    """
    book = self.find_item(title)
    if book:
        if book not in [checkout.item for checkout in self.checkouts]:  # Check if book is already checked in
            print(f"Error: Book '{title}' is not currently checked out.")
        else:
            book.available = True  # Mark book as available
            for checkout in self.checkouts:
                if checkout.item == book:
                    self.checkouts.remove(checkout)  # Remove checkout record
                    break  # Remove only the first matching checkout
            print(f"Book '{title}' successfully checked in.")
    else:
        print(f"Error: Book '{title}' not found.")

  def find_item(self, title):
        """
        Finds an item (book in this case) object based on title.

        Args:
            title (str): Title of the item to search for.

        Returns:
            Item: Item object if found, None otherwise.
        """
        for item in self.items:
            if item.title == title:
                return item
        return None


  def save_data(self):
    """
    Saves library data (items, users, checkouts) to a JSON file.
    """
    data = {
        "items": [item.to_dict() for item in self.items],
        "users": [user.to_dict() for user in self.users],
        "checkouts": [checkout.to_dict() for checkout in self.checkouts]
    }
    storage.save_data(self.filename, data)

