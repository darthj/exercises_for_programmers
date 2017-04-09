# TODO Needs to handle undetermined number of products.


def get_price_of_item():
    price_of_item = int(input("Enter the price of item: "))
    return price_of_item


def get_quantity_of_item():
    quantity_of_item = int(input("Enter the quantity of item: "))
    return quantity_of_item


def calc_base_cost(price_of_item, quantity_of_item):
    base_cost = price_of_item * quantity_of_item
    return base_cost


# subtotal = product_01 + product_02 + product_03


def calc_tax_on_subtotal(base_cost):
    tax_on_subtotal = base_cost * 0.06
    return tax_on_subtotal


# tax_total = tax_01 + tax_02 + tax_03


def calc_total_cost(base_cost, tax_on_subtotal):
    total_cost = base_cost + tax_on_subtotal
    return total_cost


def print_receipt(base_cost, tax_on_subtotal, total_cost):
    print('Subtotal: ${:,.2f}\nTax: ${:,.2f}\nTotal: ${:,.2f}'.format(
        base_cost, tax_on_subtotal, total_cost))


def main():
    price = get_price_of_item()
    quantity = get_quantity_of_item()
    base = calc_base_cost(price, quantity)
    tax = calc_tax_on_subtotal(base)
    total = calc_total_cost(base, tax)
    print_receipt(base, tax, total)


main()
