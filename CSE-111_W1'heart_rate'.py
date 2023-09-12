"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
#here is the input area, I'm asking to the users their age and making the math to find the maximim heart rate. 
age = int(input("What is your age? "))
heart_rate = 220 - age
print()

#now the massage that I want to display.
print()
print(f"Your maximum rate is {heart_rate}.")
print()
print(f"Then, during your exercise, to strengthen your heart, you should keep your heart rate between {heart_rate * 0.65} and")
print(f"{heart_rate * 0.85} of your heart's maximum rate.")
print()