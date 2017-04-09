def get_euros():
    euros = int(input("How many euros are you exchanging? "))
    return euros


def get_exchange_rate():
    exchange_rate_in_euros = float(input("What is the exchange rate? "))
    return exchange_rate_in_euros


def set_exchange_rate_of_dollar():
    exchange_rate_of_dollar = 100.00
    return exchange_rate_of_dollar


def calc_exchange_to_dollar(euros, exchange_rate_in_euros, exchange_rate_of_dollar):
    exchanged_to_dollar = euros * exchange_rate_in_euros / exchange_rate_of_dollar
    return exchanged_to_dollar


def print_results(euros, exchange_rate_in_euros, exchanged_to_dollar):
    print('{:g} euros at an exchange rate of {:,.2f} is\n${:,.2f} U.S. dollars.'.format(
         euros, exchange_rate_in_euros, exchanged_to_dollar))


def main():
    euros = get_euros()
    exchange_rate = get_exchange_rate()
    rate_of_dollar = set_exchange_rate_of_dollar()
    calculated = calc_exchange_to_dollar(euros, exchange_rate, rate_of_dollar)
    print_results(euros, exchange_rate, calculated)


main()
