# [14 of 57] Tax Calculator

### Problem Statement:

Write a simple program to compute the tax on an order amount. The program should prompt for the order amount and the state. If the state is "WI", then the order must be charged 5.5% tax. The program should display the subtotal, tax, and total for Wisonsin residents but display just the total for non-residents.

        Nouns:
            tax
            order amount
            state
            subtotal
            total
            residents
            non-residents
        
        Verbs:
            compute
            prompt
            display
        
---
### Example Output:

            What is the order amount? 10
            What is the stae? WI
            The subtotal is $10.00.
            The tax is $0.55.
            The total is $10.55.
    
        Or
    
            What is the order amount? 10
            What is the state? MN
            The total is $10.00
    
---
### Constraints:

* Implement this program using only a simple *if* statement — don't use an *else* clause.
* Ensure that all money is rounded up to the nearest cent.
* Use a single output statement at the end of the program to display the program results.

---
### Inputs, Processes, Outputs:

        Inputs:
            order amount
            state
            
        Processes:
            compute
            
        Outputs:
            subtotal
            tax
            total
              or
            just the total
---
### Test Plan:

        Inputs:
            order amount
            state
        
        Expected Results:
            What is the order amount? 10
            What is the stae? WI
            The subtotal is $10.00.
            The tax is $0.55.
            The total is $10.55.
    
        Or
    
            What is the order amount? 10
            What is the state? MN
            The total is $10.00
        
        Actual Results:
        
---
### Diagram:

![pictures](http://chet.click/upGj+)

---
###  Pseudocode:

        Pseudocode

        end

---
### Challenges:

* Allow the user to enter a state abbreviation in upper, lower, or mixed case.
* Also allow the user to enter the state's full name in upper, lower or mixed case.

---
