from models import Item, Book, User, Checkout
from library import Library  # Import the Library class
import os

def main():
  """
  Main function for the library management system.
  """
  
  # Check if previous session file exists
  if 'library_data.json' in os.listdir('.'):
    os.remove('library_data.json')

  # Create a Library instance
  library = Library()
  
  # Main loop for user interaction
  while True:
    print("\nLibrary Management System")
    print("1. Add Item")
    print("2. Update Item")
    print("3. Delete Item")
    print("4. List Items")
    print("5. Search Items")
    print("6. Add User")
    # ... (Add options for User management)
    print("7. Checkout Item")
    print("8. Checkin Item")
    print("9. Save and exit")
    print("0. Exit without Saving")

    choice = input("Enter your choice: ")

    if choice == '1':
      # Add item functionality (call Library methods)
      title = input("Enter item title: ")
      author = input("Enter author (optional): ")
      isbn = input("Enter ISBN (optional): ")
      library.add_item(Book(title, author, isbn))
    elif choice == '2':
      # Update item functionality
      title = input("Enter title of item to update: ")
      author = input("Mention Author name if you want to update Author else press enter without entering anything: ")
      if not author:
        author = None
      ISBN = input("Mention ISBN if you want to update ISBN else press enter without entering anything: ")
      if not ISBN:
        ISBN = None
      new_data = {"author": author, "ISBN": ISBN}
      library.update_item(title, new_data)
    elif choice == '3':
      # Delete item functionality
      title = input("Enter title of item to delete: ")
      library.delete_item(title)
    elif choice == '4':
      # List items functionality
      library.list_items()
    elif choice == '5':
      # Search items functionality
      title = input("Search by title (optional): ")
      author = input("Search by author (optional): ")
      isbn = input("Search by ISBN (optional): ")
      library.search_items(title, author, isbn)
    # ... (Add functionalities for User management)
    elif choice == '6':
      # List items functionality
      name = input("Enter user name: ")
      user_id = input("Enter user ID (unique): ")
      library.add_user(name, user_id)  # Call the add_user method from Library class
    elif choice == '7':
      # Checkout item functionality
      title = input("Enter title of item to checkout: ")
      user_id = input("Enter user ID: ")
      library.checkout_item(title, user_id)
    elif choice == '8':
      # Checkin item functionality
      title = input("Enter title of item to checkin: ")
      library.checkin_item(title)
    elif choice == '9':
      # Save data
      library.save_data()
      print("Data saved successfully and exit....")
      break
    elif choice == '0':
      # Exit without saving
      print("Exiting without saving...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
