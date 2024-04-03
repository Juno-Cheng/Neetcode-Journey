from functools import *
"""
LeetCode Review Notes
Date: 2024-04-03

This file contains review notes and solutions for LeetCode problems.
"""

#================== Lambda Practice

'''
Problem 1: Multiply All Numbers in a List
Goal: Use a lambda function with reduce() to multiply all numbers in a list.
Input: [1, 2, 3, 4]
Expected Output: 24
Note: You will need to import reduce() from the functools module.

'''
input = [1, 2, 3, 4]
z = reduce( lambda x,y: x * y,input) #Function uses 1 param as an accumulator. 
print(z)


'''
Problem 3: Grouping Elements Based on Length
Goal: Given a list of strings, use a lambda function within a dictionary comprehension to group them by their length.
Input: ["hello", "world", "python", "is", "awesome"]
Expected Output: {5: ["hello", "world"], 6: ["python"], 2: ["is"], 7: ["awesome"]}
Hint: You might want to use set() to find unique lengths and then group strings by length.
'''

input = ["hello", "world", "python", "is", "awesome"]
z = {x: [word for word in input if len(word) == x] for x in set(map(len, input)) }

'''
Problem: Transform to Dictionary
Given a list of tuples where each tuple contains a name followed by a score, use a lambda function to transform this list into a dictionary where each key is the name, and the value is the score multiplied by 10 if the score is below 5, and by 5 otherwise.

Example Input: [("Alice", 4), ("Bob", 6), ("Charlie", 2)]
Expected Output: {"Alice": 40, "Bob": 30, "Charlie": 20}

'''
