#this is thr area that I request a Import math to use math.pi.  
import math

#input variables here.
w = float(input("What is the width of the tire in milimiters? "))
a = float(input("What is the aspect of ratio of the tire? "))
d = float(input("What is the diameter of the wheek? "))

#the math:
h = a / 100 * w 
r = d * 25.4 / 2
v = math.pi * (w ** 2) * a * (2540 * d + w * a ) / (10 ** 10)

#result.
print()
print(f"The approximate volume is {v:.2f} liters.")