# [12 of 57] Computing Simple Interest

### Problem Statement:

Create a program that computes simple interest. Prompt for the principal amount, the rate as a percentage, and the time, and display the amount accrued (principal + interest).

    Nouns:
        simple interest
        principal amount
        rate as a percentage
        time (length of loan)
        amount accrued

    Verbs:
        computes
        prompt
        display

#### Formula:

  The formula for simple interest is *A = P(1 + rt)*, where _P_ is the principal amount, _r_ is the annual rate of interest, _t_ is the number of years the amount is invested, and _A_ is the amount at the end of the investment.

---
### Example Output:

    Enter the principal: 1500
    Enter the rate of interest: 4.3
    Enter the number of years: 4
    
    After 4 years at 4.3%, the investment will
    be worth $1758.

---
### Constraints:

* Prompt for the rate as a percentage (like 15, not .15). Divide the input by 100 in your program.
* Ensure that fractions of a cent are rounded up to the next penny.
* Ensure that the output is formatted as money.

---
### Inputs, Processes, Outputs:

    Inputs:
        principal interest
        rate as percentage
        time (length of loan)

    Processes:
        compute

    Outputs:
        display amount accrued

---
### Test Plan:

    Inputs:
        principal interest
        rate as percentage
        time (length of loan)

    Expected Results:
        Enter the principal: 1500
        Enter the rate of interest: 4.3
        Enter the number of years: 4
        
        After 4 years at 4.3%, the investment will
        be worth $1758.

    Actual Results:
    
---
### Pseudocode:

    ComputingSimpleInterest
        -Prompt for principal amount
        -Prompt for rate as percentage
        -Prompt for the time (length of loan)
        
        -Multiply rate as a percentage by time (length of loan)
        -Add 1 to the product
        -Multiply the sum by the principal amount
        
        -Display amount accrued
    end

---
### Challenges:

* Ensure that the values entered for principal, rate, and number of years are numeric and that the program will not let the user proceed without valid inputs.
* Alter the program to use a function called calculateSimpleInterest taht takes in the rate, principal, and number of years and returns the amount at the end of the investment.
* In addition to printing out the final amount, print out the amount at the end of each year.

---
