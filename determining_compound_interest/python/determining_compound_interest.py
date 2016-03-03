principal_amount = int(input("What is the principal amount? "))
rate_of_interest = float(input("What is the rate? "))
years_of_investment = int(input("What is the number of years? "))
number_of_periods = int(input("What is the number of times the interest is compounded per year? "))

value_of_investment = principal_amount * (1 + ((rate_of_interest / 100) / years_of_investment))**(years_of_investment * number_of_periods)

rate_converted_to_str = str(rate_of_interest)

print('${:d} invested at {:s}% for {:d} years\ncompounded {:d} times per year is ${:,.2f}.'.format(principal_amount, rate_converted_to_str, years_of_investment, number_of_periods, value_of_investment))