# [4 of 57] Mad Lib

### Problem Statement:

Create a simple mad-lib program that prompts for a noun, a verb, an adverb, an adjective and injects those into a story that you create.

        nouns:
        - noun
        - verb
        - adverb
        - adjective
        - story
        
        verbs:
        - prompts
        - injects
        - displays

---
### Example Output:

        Enter a noun: dog
        Enter a verb: walk
        Enter an adjective: blue
        Enter an adverb: quickly
        Do you walk your blue dog quickly?
        That's hilarious!

---
### Inputs, Processes, Outputs:

        Inputs:
        - noun
        - verb
        - adverb
        - adjective
        
        Processes:
        - prompts
        - injects
        - displays
        
        Outputs:
        - display story

---
### Test Plan:

        Inputs:
        - noun: dog
        - verb: walk
        - adjective: blue
        - adverb: quickly

        Expected Results:
          Enter a noun: dog
          Enter a verb: walk
          Enter an adjective: blue
          Enter an adverb: quickly
          Do you walk your blue dog quickly?
          That's hilarious!
        
        Actual Results:

---
### Pseudocode:

        MadLib
          -Prompt for a noun
          -Prompt for a verb
          -Prompt for an adjective
          -Prompt for an adverb
          
          -Inject into story
          
          -Display story
        end
