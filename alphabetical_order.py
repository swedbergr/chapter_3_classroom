# Get two names from the user
name1 = input("Enter a name: ")
name2 = input("Enter another name: ")

# Display names will be in alphabetical order
print("Here are the names in alphabetical order:")

# Determine alphabetical order
if name1 < name2:
  print(f"{name1}\n{name2}")
else:
  print(f"{name2}\n{name1}")