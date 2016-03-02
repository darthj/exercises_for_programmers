principal_amount = int(input("What is the principal amount? "))
rate_of_interest = float(input("What is the rate? "))
years_of_investment = int(input("What is the number of years? "))
number_of_periods = int(input("What is the number of times the interest is compounded per year? "))

interest_times_periods = (rate_of_interest / number_of_periods) + 1
exponent_interest = interest_times_periods**(number_of_periods * years_of_investment)
value_of_investment = exponent_interest * principal_amount

print('${:d} invested at {:f}% for {:d} years\ncompounded {:d} times per year is ${:,.2f}.'.format(principal_amount, rate_of_interest, years_of_investment, number_of_periods, value_of_investment))