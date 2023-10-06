#Here I Invoke a Module.
import math 

#Here is the variables function.
items = int(input("Enter the number of items: "))
per_boxes = int(input("Enter the number of items per box: "))

#Here is the math zone.
boxes_needed = math.ceil(items / per_boxes)

#The print funcion containing the result.
print()
print(f"For {items} items, packing {per_boxes} items in each box, you will need {boxes_needed} boxes.")
print()