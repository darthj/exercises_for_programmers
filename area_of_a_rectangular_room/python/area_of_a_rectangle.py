length = int(input("What is the length of the room in feet? "))
width = int(input("What is the width of the room in feet? "))

print("You entered dimensions of {:d} feet by {:d} feet.".format(length, width))

area_in_feet = width * length
area_in_meters = area_in_feet * 0.09290304

print("The area is\n{} square feet\n{} square meters".format(area_in_feet, area_in_meters))