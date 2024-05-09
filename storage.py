import json

def save_data(filename, data):
  try:
    with open(filename, 'w') as f:
      json.dump(data, f, indent=4)  # Save data with indentation for readability
  except OSError as e:
    print(f"Error saving data: {e}")

def load_data(filename):
  try:
    with open(filename, 'r') as f:
      return json.load(f)
  except FileNotFoundError:
    return {}  # Return empty dictionary if file doesn't exist
