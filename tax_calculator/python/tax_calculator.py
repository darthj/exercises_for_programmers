order_amount = int(input("What is the order amount? "))
state = input("What is the state? ")

if state == "WI":
    wi_subtotal = (order_amount * 1.00)
    wi_tax_amount = wi_subtotal * (5.5 / 100)
    wi_total = wi_subtotal + wi_tax_amount
    print("The subtotal is ${:,.2f}.\nThe tax is ${:,.2f}.\nThe total is ${:,.2f}.".format(wi_subtotal, wi_tax_amount, wi_total))


if state != "WI":
    print("The total is ${:,.2f}.".format((order_amount * 1.00)))