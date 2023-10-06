#Here We inported datetime 
from datetime import datetime

#Here we 
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

#The subtotal value.
value = float(input("Please, enter the subtotal: "))

#The discount day condition.
if day_of_week == 1 or day_of_week == 2 and value >= 50:
    value = value * 0.9
    discout = value * 0.1
    print(f"Discount amount: ${discout:.2f}")

#Here it goes the math.
tax = value * 0.06

#Here we display all the values (taxes and totoal amount).
print(f"Sales tax amount: {tax:.2f}")
print(f"Total: ${(value + tax):.2f}")