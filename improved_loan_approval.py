# Define named constants for the program
MIN_SALARY = 30000.0
MIN_YEARS = 2

# Get the potential customer's salary and years worked at current job
salary = float(input("Enter your annual salary: "))
years_worked = float(input("Enter the number of years worked at your current job: "))

# Check if salary is large enough
if (salary >= MIN_SALARY) and (years_worked >= MIN_YEARS):
  # Inform customer that he/she is approved for the loan
  print("You qualify for the loan.")
else:
  # Respond with denial to request due to salary
  print("You do not qualify for the loan.")