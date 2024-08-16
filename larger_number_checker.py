# Get two numbers from the user to compare
num1 = float(input("What is the first number to compare? "))
num2 = float(input("What is the second number to compare? "))

# Assign larger number to new variable
greatest = num1 if num1 > num2 else num2

# Display larger number
print(greatest)