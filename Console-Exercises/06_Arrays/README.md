# 05 ARRAYS

This folder contains exercises on the use of lists.

================================================================================

06_01_SearchNum
* Prompt user for 20 numbers
  - Check for valid input
* Output filled array
* Prompt user for a searched number
  - Check user for valid input
* loop through array and count searched number in array
* add index of where searched number was found to new array
* print count and index of searched numbers

06_02_Statistics
* Prompt user for amount of throws 
  - check vor valid input
* Print result of every throw
* Optimize readability
  - give every number a diffrent color
  - print indexes of columns and lines
* Summarize results

06_03_StudentScoreManager
* Give user options:
  - Add student
  - Add score of a subject to student
  - Show student average
  - Show all students
  - Exit
* Add student
  - Prompt for name
  - Check for valid input (not empty)
  - Assign unique ID
  - Store student in list
  - Initialize empty score dictionary for student
* Add score of a subject to student
  - Show available students
  - Prompt for student ID
  - Check for valid ID
  - Prompt for subject
  - Check for valid input
  - Prompt for score (0–100)
  - Check for valid input and range
  - Append score to subject list
* Show student average
  - Show available students
  - Prompt for student ID
  - Check for valid ID
  - Collect all subject scores
  - Calculate average
  - Print result (rounded to 2 decimals)
  - If no scores → print message
* Show all students
  - Print ID
  - Print name
  - Print subjects and scores
* Exit program

06_04_OnlyFrom0To25
* Prompt user repeatedly for digits
* only stop loop if user enters nothing
* strip the list of negative or above 25 numbers
* square remaining numbers and output

06_05_ScoreAnalysis
* Given predefined list of scores
* Calculate total score
  - loop through list
  - sum values
* Calculate average
  - total / amount
  - print result
* Find lowest and highest
  - compare each value
  - update min and max
  - print results
* Sort scores (bubble sort)
  - copy list
  - nested loop
  - swap if left > right
  - print sorted list