username = input("username: ")

def validate_username(name):
  if len(username) > 12:
    return "your username must be no longer than 12 characters"
  if not username.isalpha():
    return "your username must not contain numbers or spaces"
  return "your username has been accepted"

print(validate_username(username))

