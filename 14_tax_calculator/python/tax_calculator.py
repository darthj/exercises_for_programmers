def get_order_amount():
    order_amount = int(input("What is the order amount? "))
    return order_amount


def get_state():
    state = input("What is the state? ")
    return state


def calc_tax(order_amount, state):
    if state == "WI":
        wi_subtotal = (order_amount * 1.00)
        wi_tax_amount = wi_subtotal * (5.5 / 100)
        wi_total = wi_subtotal + wi_tax_amount
        print("The subtotal is ${:,.2f}.\nThe tax is ${:,.2f}.\nThe total is ${:,.2f}.".format(
            wi_subtotal, wi_tax_amount, wi_total))
    else:
        print("The total is ${:,.2f}.".format((order_amount * 1.00)))


def main():
    order_amount = get_order_amount()
    state = get_state()
    calc_tax(order_amount, state)


main()
