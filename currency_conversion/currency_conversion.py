import math

euros = float(input("How many euros are you exchanging? "))
exchange_rate_in_euros = float(input("What is the exchange rate? "))

euro_and_rate = euros * exchange_rate_in_euros
exchanged_to_dollar = euro_and_rate / 0.92

print('{:,.2f} euros at an exchange rate of {:,.2f} is\n${:,.2f} U.S. dollars.'.format(euros, exchange_rate_in_euros, exchanged_to_dollar))
