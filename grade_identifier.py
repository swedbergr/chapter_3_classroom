# Define named constants for the program
A_MIN = 90
B_MIN = 80
C_MIN = 70
D_MIN = 60

# Get grade from user
grade = float(input("What is the grade you earned? "))

# Conditional statements for grade
if grade >= A_MIN:
  print("Your grade is A.")
elif grade >= B_MIN:
  print("Your grade is B.")
elif grade >= C_MIN:
  print("Your grade is C.")
elif grade >= D_MIN:
  print("Your grade is D.")
else:
  print("Your grade is F.")