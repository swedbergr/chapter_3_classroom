# Define named constants for overtime threshold and overtime rate multiplier
OVERTIME_THRESHOLD = 40
OVERTIME_RATE = 1.5

# Get the number of hours worked
hours_worked = float(input("How many hours did you work? "))

# Get the hourly pay rate
hourly_rate = float(input("What is your hourly pay rate? "))

# Define variable for overtime hours worked and overtime rate
overtime_hours = 0
overtime_pay_rate = hourly_rate * OVERTIME_RATE

# Check if the employee worked any overtime hours
if hours_worked > OVERTIME_THRESHOLD:
  overtime_hours = hours_worked - OVERTIME_THRESHOLD
  hours_worked = OVERTIME_THRESHOLD

# Calculate gross income
gross_income = hourly_rate * hours_worked + overtime_hours * overtime_pay_rate


# Display gross income
print(f"Your gross income is {gross_income}")