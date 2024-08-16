# Set threshold for needing a coat
COAT_THRESHOLD = 50

# Check temperature outside from user
temp = float(input("What is the temperature outside in degrees Fahrenheit? "))

# Determine of a coat is needed
if temp < COAT_THRESHOLD:
  print("Grab a coat.", end = " ")

# Leave user with greeting
print("Enjoy outside!")