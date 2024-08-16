# Define named constants for the program
MIN_SALARY = 30000.0
MIN_YEARS = 2

# Get the potential customer's salary and years worked at current job
salary = float(input("Enter your annual salary: "))
years_worked = float(input("Enter the number of years worked at your current job: "))

# Check if salary is large enough
if salary >= MIN_SALARY:
  # Check if the minimum number of years worked is also enough
  if years_worked >= MIN_YEARS:
    # Inform customer that he/she is approved for the loan
    print("You qualify for the loan.")
  else:
    # Respond with denial to request due to years worked
    print("You must have been at your current job at least two years to qualify.")
else:
  # Respond with denial to request due to salary
  print("You must earn at least $30,000 per year to qualify.")