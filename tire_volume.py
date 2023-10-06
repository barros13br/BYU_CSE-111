#this is thr area that I request a Import math to use math.pi.  
import math
from datetime import datetime 

#input variables here.
w = float(input("What is the width of the tire in milimiters? "))
a = float(input("What is the aspect of ratio of the tire? "))
d = float(input("What is the diameter of the wheek? "))
current_date_and_time = datetime.now()

#the math:
h = a / 100 * w 
r = d * 25.4 / 2
v = math.pi * (w ** 2) * a * (2540 * d + w * a ) / (10 ** 10)

#result.
print()
print(f"The approximate volume is {v:.2f} liters.")

#here is were the file volumes.txt is open and is save. 
with open("volumes.txt", "at") as adding:
    print(f"{current_date_and_time:%Y-%m-%d}", int(w), int(a), int(d), f"{v:.2f}", sep=", ", file=adding)