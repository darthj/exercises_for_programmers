import math

length = int(input("What is the length?"))
width = int(input("What is the width? "))

area_of_ceiling = length * width
paint_needed = area_of_ceiling / 350
paint_rounded = math.ceil(paint_needed)

print("You will need to purchase {} gallons of paint to cover {} square feet.".format(paint_rounded, area_of_ceiling))
