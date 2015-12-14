# [7 of 57] Area of a Rectangular Room

### Problem Statement:

Create a program that calculates the area of a room. Prompt the user for the length and width of the room in feet. Then display the area in both square feet and square meters.

        Nouns:
          length
          width
          area
          
        Verbs:
          calculate
          prompt
          display

___
### Example Output:

        What is the length of the room in feet? 15
        What is the width of the room in feet? 20
        You entered dimensions of 15 feet by 20 feet.
        The area is
        300 square feet
        27.871 square meters
        
---
### Inputs, Processes, Outputs:

        Inputs:
          length
          width
          
        Processes:
          calculate
          
        Output:
          area

---
### Test Plan:

        Inputs:
          - length: 15
          - width: 20
          
        Expected Results:
          What is the length of the room in feet? 15
          What is the width of the room in feet? 20
          You entered dimensions of 15 feet by 20 feet.
          The area is
          300 square feet
          27.871 square meters
          
        Actual Results:

---
### Pseudocode:

        RectangularRoom
          - Prompt for length
          - Prompt for width
          
          - Multiply width by length
          - Multiply product by 0.09290304
          
          - Display area in feet
          - Display area in meters
        end
