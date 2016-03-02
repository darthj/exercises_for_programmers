euros = int(input("How many euros are you exchanging? "))
exchange_rate_in_euros = float(input("What is the exchange rate? "))

exchange_rate_of_dollar = 100.00

exchanged_to_dollar = euros * exchange_rate_in_euros / exchange_rate_of_dollar

print('{:g} euros at an exchange rate of {:,.2f} is\n${:,.2f} U.S. dollars.'.format(euros, exchange_rate_in_euros, exchanged_to_dollar))
