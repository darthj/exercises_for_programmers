euros = int(input("How many euros are you exchanging? "))
exchange_rate_in_euros = float(input("What is the exchange rate? "))

exchanged_to_dollar = euros * exchange_rate_in_euros / 100.0

print('{:g} euros at an exchange rate of {:,.2f} is\n${:,.2f} U.S. dollars.'.format(euros, exchange_rate_in_euros, exchanged_to_dollar))
