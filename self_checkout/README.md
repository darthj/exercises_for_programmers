# [0 of 57] Self Checkout

### Problem Statement:

Create a simple self-checkout system. Prompt for prices and quantities of three items. Calculate the subtotal of the items. Then calculate the tax using a tax rate of 5.5% Print out the line items with the quantity and total, and then print out the subtotal, tax amount, and total.

    Nouns:
        prices
        quantities
        subtotal
        tax rate
        total

    Verbs:
        prompt
        calculate
        print

---
### Example Output:

    Enter the price of item 1: 25
    Enter the quantity of item 1: 2
    Enter the price of item 2: 10
    Enter the quantity of item 2: 1
    Enter the price of item 3: 4
    Enter the quantity of item 3: 1
    Subtotal: $64.00
    Tax: $3.52
    Total: $67.52

---
### Constraints:

* Keep the input, processing, and the output parts of your program separate. Collect the input, then do the math operations and string building, and then print out the output.
* Be sure you explicitly convert input to numerical data before doing any calculations.

---
### Inputs, Processes, Outputs:

    Inputs:
        prices
        quantities

    Processes:
        calculate

    Outputs:
        quantity
        subtotal
        tax amount
        total

---
### Test Plan:

    Inputs:
        prices
        quantities

    Expected Results:
        Enter the price of item 1: 25
        Enter the quantity of item 1: 2
        Enter the price of item 2: 10
        Enter the quantity of item 2: 1
        Enter the price of item 3: 4
        Enter the quantity of item 3: 1
        Subtotal: $64.00
        Tax: $3.52
        Total: $67.52

    Actual Results:

---
### Pseudocode:

    Pseudocode
        -Prompt for price of item
        -Prompt for quantity of item
        
        -Repeat previous steps two more times
        
        -Multiply the price of the items by quantities of items
        -Multiply that product by the tax rate
        
        -Display each item's quantity and total
        -Display the subtotal
        -Display the tax amount
        -Display the total
    end

---
### Challenges:

* Revise the program to ensure that prices and quantities are entered as numeric values. Don't allow the user to proceed if the value entered is not numeric.
* Alter the program so that an indeterminate number of items can be entered. The tax and total are computed when there are no more items to be entered.

---
