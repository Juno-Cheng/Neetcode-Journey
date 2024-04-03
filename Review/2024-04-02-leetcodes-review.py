"""
LeetCode Review Notes
Date: 2024-04-02

This file contains review notes and solutions for LeetCode problems.
"""

#================== Lambda Practice
'''
Problem: Intersection of Two Lists
Given two lists of numbers, use a lambda function within a filter() call to find the intersection of the two lists (elements present in both lists).

Example Input: [1, 2, 3, 4, 5], [4, 5, 6, 7, 8]
Expected Output: [4, 5]
'''

x,y = [1, 2, 3, 4, 5], [4, 5, 6, 7, 8]
z = filter(lambda x: x in y, x)
print(list(z))


'''
Convert Temperatures
Use: map()
Description: Given a list of temperatures in Celsius, use a lambda function with map() to
convert them to Fahrenheit. The formula to convert Celsius to Fahrenheit is (C * 9/5) + 32.

Example Input: [0, 10, 20, 30]
Expected Output: [32.0, 50.0, 68.0, 86.0]
'''

input =  [0, 10, 20, 30]
y = map(lambda x: (x * 9/5) + 32, input)
print(list(y))


'''
Problem : Find Lengths of Strings
Given a list of strings, create a list containing the lengths of each string.

Example Input: ["hello", "world", "python", "is", "awesome"]
Expected Output: [5, 5, 6, 2, 7]
'''

input =  ["hello", "world", "python", "is", "awesome"]
y = map(lambda x: len(x), input)
print(list(y))


'''
Problem: Extract Names of People Over 20 Years Old
Input: A list of dictionaries: [{"name": "Alice", "age": 17}, {"name": "Bob", "age": 21}, {"name": "Cathy", "age": 19}, {"name": "Dave", "age": 22}]
Expected Output: A list of names of people over 20 years old: ["Bob", "Dave"]
'''

input =  [{"name": "Alice", "age": 17}, {"name": "Bob", "age": 21}, {"name": "Cathy", "age": 19}, {"name": "Dave", "age": 22}]
input2 = filter(lambda x: x["age"] > 20, input)
y = map(lambda x: x["name"], list(input2))
print(list(y))

'''
Problem: Transform to Dictionary
Given a list of tuples where each tuple contains a name followed by a score, use a lambda function to transform this list into a dictionary where each key is the name, and the value is the score multiplied by 10 if the score is below 5, and by 5 otherwise.

Example Input: [("Alice", 4), ("Bob", 6), ("Charlie", 2)]
Expected Output: {"Alice": 40, "Bob": 30, "Charlie": 20}

'''


