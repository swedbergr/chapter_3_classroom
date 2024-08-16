# Define named constant for passing threshold
PASSING_THRESHOLD = 0.7

# Get points earned and total points from the user
points_earned = float(input("How many points were earned? "))
points_total = float(input("How many points were available? "))

# Calculate the grade as a percentage
grade_percent = points_earned / points_total

# Check if the student passed and display message accordingly
if grade_percent < PASSING_THRESHOLD:
  print(f"You received a {grade_percent:.1%}.")
  print(f"Adjust your study habbits so you can do better next time.")
else:
  print(f"You received a {grade_percent:.1%}.")
  print(f"Your study habbits appear to be working well.")