# [16 of 57] Legal Driving Age

### Problem Statement:

Write a program that asks the user for their age and compare it to the legal driving age of sixteen. If the user is sixteen or older, then the program should display “You are old enough to legally drive.” If the user is under sixteen, the program should display “You are not old enough to legally drive."

        Nouns:
            age
            legal driving age of sixteen
        
        Verbs:
            compare
            display
        
---
### Example Output:

        What is your age? 15
        You are not old enough to legally drive.
        
        Or
        
        What is your age? 35
        You are old enough to legally drive.
              
---
### Constraints:

        * Use a single output statement.
        * Use a ternary operator to write this program. If your language doesn’t support a ternary operator, use a regular if/else statement, and still use a single output statement to display the message.

---
### Inputs, Processes, Outputs:

        Inputs:
            age
                
        Processes:
            compare
                
        Outputs:
            “You are old enough to legally drive.”
            or
            “You are not old enough to legally drive."

                
---
### Test Plan:

        Inputs:
        
        Expected Results:
          
        Actual Results:
        
---
###  Pseudocode:

        LegalDrivingAge
	    Prompt user for their age.

	    Compare their age with the legal driving age.

	    If their age is >= sixteen, print "You are old enough to legally drive."

	    Else print "You are not old enough to legally drive."
        end

---
### Challenges:

	* If the user enters a number that's less than zero or enters non-numeric data, display an error message that asks the user to enter a valid age.
	* Instead of hard-coding the driving age in your program logic, research driving ages for various countries and create a lookup table for the driving ages and countries. Prompt for the age, and display which countries the user can legally drive in.
---