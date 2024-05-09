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
