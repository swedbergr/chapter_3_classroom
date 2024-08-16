# Get grade year from user
grade_year = input("What grade are you in this school year? ")

# Assign graduation variable
graduation = True

# Check if graduation is true
if not (grade_year == "12" or grade_year == "senior"):
  graduation = False

if graduation:
  print("Congratulations!")
else:
  print("Hang in there...")
