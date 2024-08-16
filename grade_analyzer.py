# Get 3 grades from user
grade_1 = float(input("Enter the first grade: "))
grade_2 = float(input("Enter the second grade: "))
grade_3 = float(input("Enter the third grade: "))

# Determine which grade is the highest
highest_grade = grade_1
if highest_grade < grade_2:
  highest_grade = grade_2

if highest_grade < grade_3:
  highest_grade = grade_3

# Display the highest grade
print(f"The highest grade is {highest_grade}.")