def get_principal_amount():
    principal_amount = int(input("Enter the principal: "))
    return principal_amount


def get_rate_of_exchange():
    rate_of_interest = float(input("Enter the rate of interest: "))
    return rate_of_interest


def get_time_of_loan():
    time_of_loan = int(input("Enter the number of years: "))
    return time_of_loan


def calc_value_of_investment(rate_of_interest, time_of_loan, principal_amount):
    value_of_investment = ((rate_of_interest / 100) * time_of_loan + 1) * principal_amount
    return value_of_investment


def convert_rate_to_string(rate_of_interest):
    rate_converted_to_str = str(rate_of_interest)
    return rate_converted_to_str


def print_results(time_of_loan, rate_converted_to_str, value_of_investment):
    print("After {:d} years at {:s}%, the investment will\nbe worth ${:,.2f}".format(
        time_of_loan, rate_converted_to_str, value_of_investment))


def main():
    amount = get_principal_amount()
    rate = get_rate_of_exchange()
    time = get_time_of_loan()
    value = calc_value_of_investment(rate, time, amount)
    converted = convert_rate_to_string(rate)
    print_results(time, converted, value)


main()
