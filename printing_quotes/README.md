# [3 of 57] Printing Quotes

### Problem Statement:

Create a program that prompts for a quote and an author. Display the quotation and author as shown in the example output.

        nouns:
        - quote
        - author
        
        verbs:
        - prompts
        - display

---
### Example Output:
        
        What is the quote? These aren't the droids you're looking for.
        Who said it? Obi-Wan Kenobi
        Obi-Wan Kenobi says, "These aren't the droids you're looking for."

---
### Inputs, Processes, Outputs:
        
        Inputs:
        - quote and author
        
        Processes:
        - prompts and displays
        
        Outputs:
        - author and quotation

---
### Test Plan:
        
        Inputs:
        - quote: These aren't the droids you're looking for.
        - author: Obi-Wan Kenobi
        
        Expected Result:
          Obi-Wan Kenobi says, "These aren't the droids you're looking for."
        
        Actual Results:

---
### Pseudocode
        
        QuotePrinter
          - Prompts for a quote "What is the quote?"
          - Prompts for author "Who said it?"
          
          - Combine quote and author, using _escape characters_ to handle quotations.
          
          - Display author and quote.
        end
