# [11 of 57] Currency Conversion

### Problem Statement:

Write a program that converts currency. Specifically, convert euros to U.S. dollars. Prompt for the amount of money in euros you have, and prompt for the current exchange rate of the euro. Print out the new amount in U.S. dollars. 

        Nouns:
            euros
            U.S. dollars
            exchange rate euros
            exchange rate dollars

        Verbs:
            convert
            prompt
            print
 
 #### Formula:
 
 The formula for currency conversion is 
![Currency Conversion Formula](http://www.mathinary.com/image.jsp?formula=amount_%7Bto%7D+%3D+%5Cfrac%7Bamount_%7Bfrom%7D+%5Ctimes+rate_%7Bfrom%7D%7D%7Brate_%7Bto%7D%7D)
where
* _Amount to_ is the amount in U.S. dollars.
* _Amount from_ is the amount in euros.
* _rate from_ is the current exchange rate in euros.
* _rate to_ is the current exhange rate of the U.S. dollar.

---
### Example Output:

    How many euros are you exchanging? 81
    What is the exchange rate? 137.51
    81 euros at an exchange rate of 137.51 is
    111.38 U.S. dollars.

---
### Constraints:

* Ensure that fractions of a cent are rounded up to the next penny.
* Use a single output statement.

---
### Inputs, Processes, Outputs:

    Inputs:
        euros
        dollars
        exchange rate

    Processes:
        convert

    Outputs:
        dollars

---
### Test Plan:

    Inputs:
        euros
        dollars
        exchange rate

    Expected Results:
        How many euros are you exchanging? 81
        What is the exchange rate? 137.51
        81 euros at an exchange rate 137.51 is
        111.38 U.S. dollars.

    Actual Results:

---
### Pseudocode:

    CurrencyConversion
        -Prompt for amount of money in euros you have
        -Prompt for current exchange rate in euros
        
        -Multiply euros by the exchange rate of the euro
        -Divide the product by exchange rate of the dollar
        
        -Print new amount
    end
