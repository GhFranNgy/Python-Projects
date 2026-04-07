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

06_06_FruitCounter
* Initialize list of various fruits
* Create a set of unique fruit types
* Count occurrences of each fruit
  - Initialize empty dictionary for counts
  - Loop through list
  - Increment count if fruit exists, otherwise initialize to 1
* Identify the most frequent fruit
  - Initialize variables for most common fruit and highest count
  - Iterate through the dictionary
  - Compare current count to highest recorded count
  - Update highest count and most common fruit name
* Output result
  - Print original list
  - Print unique fruit kinds
  - Print the dictionary of counts
  - Print the most common fruit found

06_07_OddorEven
* Initialize list of numbers
* loop trough list
  - if number is even check if even array exists if not create new
  - if number is odd check if odd array exists if not create new
* Output sorted dict
* RESTRICTION: use a dict, start with empty dict

06_08_4DataStructures
* Copy data into list with no duplicates
* filter unique items with a set
* store items in tuple
* Count occurrences of each item
  - Initialize empty dictionary
  - Loop through original list
    - If item exists in dictionary increment count
    - Else initialize count to 1

06_09_GroupByLength
* Prompt user for a sentence. split into words
* Strip spaces/punctuation from each word
* Initialize empty dictionary
* Loop through words:
  - length = len(word)
  - if length in dict append word
  - else create new list with word
* Convert each list to tuple
* Print dictionary

06_10_WordLengthTracker
* Prompt user for a sentence
  - Check for valid input
* Split sentence into words
  - Strip punctuation from each word
* Initialize dictionaries
  - group words by length
  - count word occurrences
* Loop through words
  - If length exists then append word
  - Else create new list with word
  - If word exists then increment count
  - Else initialize count to 1
* Find most common word
  - Initialize highest_count = 0
  - Loop through occurence_Words
  - If count > highest_count then update values
* Output results
  - Print most common word
  - Print dictionary grouped by length
  - Print dictionary of word counts