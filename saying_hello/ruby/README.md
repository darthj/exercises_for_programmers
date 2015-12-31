# [1 of 57] Saying Hello

### Problem Statement:

Create a program that prompts for your name and prints a greeting using your name.

| Nouns    | Verbs   |
|----------|:--------|
| name     | prompts |
| greeting | prints  |

---
### Example Output:

        What is your name? Chet
        Hello, Chet, nice to meet you!

---
### Inputs, Processes, Outputs:

| Inputs | Processes | Outputs  |
|--------|:----------|:---------|
| name   | prompts   | greeting |
|        | prints    |          |

---
### Test Plan:

        Inputs:
          name: Brian
          
        Expected Results:
          What is your name? Chet
          Hello, Chet, nice to meet you!
          
        Actual Results:
        
---
### Pseudocode:

        SayHello
          - Prompt for name with "What is your name?"
          
          - Greeting = "Hello," + name + ", nice to meet you."
          
          - Display greeting
        end