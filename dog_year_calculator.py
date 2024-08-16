# Set constant for dog-year conversion
DOG_YEAR_CONVERSION = 7

# Get age from the user
human_age = input("What is your age in years? ")

# Re-prompt for human_age if user does not input a number
if not human_age.isdigit():
  human_age = input(f"{human_age} is not a number. What is your age in years? ")

# Cast age to float
human_age = float(human_age)

# Compute dog-year age
dog_age = human_age * DOG_YEAR_CONVERSION

# Print age in dog years for user
print(f"Your age in dog years is {dog_age:.1f}")