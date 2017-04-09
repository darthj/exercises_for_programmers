import math


def get_length():
    length = int(input("What is the length? "))
    return length


def get_width():
    width = int(input("What is the width? "))
    return width


def area_formula(length, width):
    area_of_ceiling = length * width
    return area_of_ceiling


def calc_paint_needed(area_of_ceiling):
    paint_needed = area_of_ceiling / 350
    return paint_needed


def calc_paint_rounded(paint_needed):
    paint_rounded = math.ceil(paint_needed)
    return paint_rounded


def print_results(paint_rounded, area_of_ceiling):
    print("You will need to purchase {} gallons of paint to cover {} square feet.".format(
        paint_rounded, area_of_ceiling))


def main():
    lengthed = get_length()
    widthed = get_width()
    area = area_formula(lengthed, widthed)
    needed = calc_paint_needed(area)
    rounded = calc_paint_rounded(needed)
    print_results(rounded, area)


main()
