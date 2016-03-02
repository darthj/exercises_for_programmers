principal_amount = int(input("Enter the principal: "))
rate_of_interest = float(input("Enter the rate of interest: "))
time_of_loan = int(input("Enter the number of years: "))

value_of_investment = ((rate_of_interest / 100) * time_of_loan + 1) * principal_amount

print("After {:d} years at {:f}%, the investment will\nbe worth ${:f}".format(time_of_loan, rate_of_interest, value_of_investment))