# Define named constant
ADULT = 18

# Get age and check it for user
if (age := int(input("What is your age? "))) >= ADULT:
  print("You are an adult.")
else:
  print("You are a minor.")

print(age)