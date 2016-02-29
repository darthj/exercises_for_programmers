import math

price_of_item_01 = int(input("Enter the price of item 1: "))
quantity_of_item_01 = int(input("Enter the quantity of item 1: "))
price_of_item_02 = int(input("Enter the price of item 2: "))
quantity_of_item_02 = int(input("Enter the quantity of item 2: "))
price_of_item_03 = int(input("Enter the price of item 3: "))
quantity_of_item_03 = int(input("Enter the quantity of item 3: "))

product_01 = price_of_item_01 * quantity_of_item_01
product_02 = price_of_item_02 * quantity_of_item_02
product_03 = price_of_item_03 * quantity_of_item_03

subtotal = product_01 + product_02 + product_03

tax_01 = product_01 * 0.06
tax_02 = product_02 * 0.06
tax_03 = product_03 * 0.06

tax_total = tax_01 + tax_02 + tax_03

total = subtotal + tax_total

print('Subtotal: ${:,.2f}\nTax: ${:,.2f}\nTotal: ${:,.2f}'.format(subtotal, tax_total, total))