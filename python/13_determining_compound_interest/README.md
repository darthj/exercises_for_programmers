# [13 of 57] Determining Compound Interest

### Problem Statement:

Write a program to compute the value of an investment compounded over time. The program should ask for the starting amount, the number of years to invest, the interest rate, and the number of periods per year to compound.

        Nouns:
            value of investment
            principal amount
            rate of interest
            number of years
            number of periods
        
        Verbs:
            compute
            prompt
            display
        
#### Formula:

![compound interest formula](http://www.purplemath.com/modules/logs/expfcn07.gif)

where
* _P_ is the principal amount.
* _r_ is the annual rate of interest.
* _t_ is the number of years the amount is invested.
* _n_ is the number of times the interest is compounded per year.
* _A_ is the amount at the end of the investment.

---
### Example Output:

        What is the principal amount? 1500
        What is the rate? 4.3
        What is the number of years? 6
        What is the number of times the interest
        is compounded per year? 4
        $1500 invested at 4.3% for 6 years
        compounded 4 times per year is $1938.84.
        
---
### Constraints:

* Prompt for the rate as a percentage (like 15, not .15). Divide the input by 100 in your program.
* Ensure that fractions of a cent are rounded up to the next penny.
* Ensure that the output is formatted as money.

---
### Inputs, Processes, Outputs:

        Inputs:
            principal amount
            rate of interest
            number of years
            number of periods
            
        Processes:
            compute
            prompt
            display
            
        Outputs:
            amount at the end
            
---
### Test Plan:

        Inputs:
            principal amount
            rate of interest
            number of years
            number of periods
        
        Expected Results:
            What is the principal amount? 1500
            What is the rate? 4.3
            What is the number of years? 6
            What is the number of times the interest
            is compounded per year? 4
            $1500 invested at 4.3% for 6 years
            compounded 4 times per year is $1938.84.
        
        Actual Results:
        
---
###  Pseudocode:

        DeterminingCompoundInterest
            -Prompt for principal amount
            -Prompt for number of years to invest
            -Prompt for rate of interest
            -Prompt for number of periods per year to compound
            
            -Divide rate of interest by number of periods
            -Add 1 to the quotient
            -Raise the sum by the product of number of periods multiplied by the number of years
            -Multiply that by the principle
            
            -Display the value of investment
        end

---
### Challenges:

* Ensure that all of the inputs are numeric and that the program will not let the user proceed without valid inputs.
* Create a version of the program that works in reverse, so you can determine the initial amount you’d need to invest to reach a specific goal.
* Implement this program as a GUI app that automatically updates the values when any value changes.

---
