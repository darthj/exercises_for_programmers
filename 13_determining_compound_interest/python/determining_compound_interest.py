# TODO PEP8 violations on line length


def get_principal_amount():
    principal_amount = int(input("What is the principal amount? "))
    return principal_amount


def get_rate_of_interest():
    rate_of_interest = float(input("What is the rate? "))
    return rate_of_interest


def get_years_to_invest():
    years_to_invest = int(input("What is the number of years? "))
    return years_to_invest


def get_number_of_periods():
    number_of_periods = int(
        input("What is the number of times the interest is compounded per year? "))
    return number_of_periods


def calc_value_of_interest(
    principal_amount,
    rate_of_interest,
    years_to_invest,
    number_of_periods
        ):
    value_of_investment = principal_amount * (
        1 + ((rate_of_interest / 100) / years_to_invest))**(
            years_to_invest * number_of_periods)
    return value_of_investment


def convert_rate_to_string(rate_of_interest):
    rate_converted_to_str = str(rate_of_interest)
    return rate_converted_to_str


def print_results(
    principal_amount,
    rate_converted_to_str,
    years_to_invest,
    number_of_periods,
    value_of_investment
        ):
    print(
        '${:d} invested at {:s}% for {:d} years\ncompounded {:d} times per year is ${:,.2f}.'.format(
            principal_amount,
            rate_converted_to_str,
            years_to_invest,
            number_of_periods,
            value_of_investment))


def main():
    principal = get_principal_amount()
    rate = get_rate_of_interest()
    years = get_years_to_invest()
    periods = get_number_of_periods()
    interest_calculated = calc_value_of_interest(principal, rate, years, periods)
    converted = convert_rate_to_string(rate)
    print_results(principal, converted, years, periods, interest_calculated)


main()
