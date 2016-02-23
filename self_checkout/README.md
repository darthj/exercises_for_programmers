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
        
        -Multiply the price of the items by quantities of items
        -Multiply that product by the tax rate
        
        -Repeat above process two more times
        
        
    end
