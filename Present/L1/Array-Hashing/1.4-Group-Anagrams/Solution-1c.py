#https://leetcode.com/problems/group-anagrams/description/
'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Constraints:
1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.

Recommended Time & Space Complexity
You should aim for a solution with O(m * n) time and O(m) space, where m is the number of strings and n is the length of the longest string.

Topics:
- Arrays
- Hash Table
- Sorting
- Strings


'''
#Default Libraries ------------- Try to get 99% Percentile Time/Space
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import unittest
from typing import List

'''
======================================
Basic Restrictions: 
Built-In Functions Allowed: Use Python's built-in dictionary operations (get, items) and tuple().
Data Structures Allowed: Dictionaries for character counting and grouping anagrams.

Algorithmic Restrictions
Character Counting Approach: Count character frequencies using a fixed-size array instead of sorting the entire string.
Hash Map Approach: Use a dictionary where keys are character frequency representations and values are lists of anagrams.
Single Pass: Group all anagrams in a single traversal of the input array.

Language/Implementation Restrictions
Character Counting: Use a fixed-size array (26 elements) with ord() to count occurrences (O(n) time, more efficient than sorting).
Hashable Keys: Convert the mutable array to an immutable string using str(array) for use as dictionary key.
Array Immutability: Arrays (lists) cannot be dictionary keys (not hashable), so convert to string.
Key Creation: Use str(char_array) to create a consistent, hashable key representation.

Hard Mode
No Dictionary for Counting: Use a fixed-size array with ord() to count characters (26 elements for lowercase).
No Sorting: Avoid sorting dictionary items by using a fixed-size array converted directly to tuple.
Constant Space Key: Use tuple of 26 integers instead of tuple of variable-length items.
No Built-In Tuple: Manually create hashable key representation.

======================================
Thought Process:
- Character Counting with Array-to-String Keys
Counting character frequencies is more efficient than sorting (O(n) vs O(n log n)). Use a fixed-size array 
of 26 elements (for lowercase a-z) with ord() to map characters to indices. Count each character in O(n) 
time. The challenge is converting the mutable array to an immutable key for the dictionary. Convert the 
array to a string using str(array), which creates a hashable key. This approach achieves O(n) counting 
per string without any sorting overhead. The key insight is understanding immutability requirements for 
dictionary keys and finding the right conversion method.
Time Complexity - O(m * n) where m is number of strings and n is average string length (counting is O(n), no sorting needed)
Space Complexity - O(m * n) where m is number of strings and n is average string length (storing all strings)
Note: Had to look up help for the immutability conversion - this is part of learning! Revisit in a week to reinforce.
'''

class Solution: # Built-In
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # While sorting takes O(n), but O(nlogm), we can instead just count the letters like in Anagrams
        group_dict = {}
        for string in strs:
            char_dict = [0] * 26
            for let in string:
                char_dict[ord(let) - ord('a')] += 1
            group_dict[str(char_dict)] =  group_dict.get(str(char_dict), [])
            group_dict[str(char_dict)].append(string)

        return list(group_dict.values())

'''
Note to Self:
This is like our C Class with Darrell Long.
This is the same pattern as bitwise manipulation and bitmasking.

Store [True, False, True, False, False, True, False, False] (8 booleans = ~8 bytes)
Store 0b10100100 (8 bits = 1 byte)

We can use this to store the frequency of the characters in the string.
It is simply a form of state representation, but instead of using booleans, we use integers. 0/1 to 0-25 for the characters a-z.
'''

        

# Test Cases ======================================
class UnitTest(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Solution class for testing
        self.solution = Solution()
    
    def test_basic_example_1(self):
        strs = ["act", "pots", "tops", "cat", "stop", "hat"]
        result = self.solution.groupAnagrams(strs)
        # Sort each group and the result for comparison (order doesn't matter)
        result = [sorted(group) for group in result]
        result.sort()
        expected = [sorted(["hat"]), sorted(["act", "cat"]), sorted(["stop", "pots", "tops"])]
        expected.sort()
        self.assertEqual(result, expected, "Should group anagrams correctly")
    
    def test_basic_example_2(self):
        strs = ["x"]
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(result, [["x"]], "Should handle single string")
    
    def test_empty_string(self):
        strs = [""]
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(result, [[""]], "Should handle empty string")
    
    def test_multiple_empty_strings(self):
        strs = ["", ""]
        result = self.solution.groupAnagrams(strs)
        # Sort result for comparison
        result = [sorted(group) for group in result]
        self.assertEqual(result, [["", ""]], "Should group multiple empty strings together")
    
    def test_no_anagrams(self):
        strs = ["abc", "def", "ghi"]
        result = self.solution.groupAnagrams(strs)
        # Sort result for comparison
        result = [sorted(group) for group in result]
        result.sort()
        expected = [sorted(["abc"]), sorted(["def"]), sorted(["ghi"])]
        expected.sort()
        self.assertEqual(result, expected, "Should return separate groups when no anagrams exist")
    
    def test_all_same_anagrams(self):
        strs = ["eat", "tea", "ate"]
        result = self.solution.groupAnagrams(strs)
        # Sort result for comparison
        result = [sorted(group) for group in result]
        self.assertEqual(len(result), 1, "Should have one group")
        self.assertEqual(sorted(result[0]), sorted(["eat", "tea", "ate"]), "Should group all anagrams together")
    
    def test_single_character_strings(self):
        strs = ["a", "b", "a", "c", "b"]
        result = self.solution.groupAnagrams(strs)
        # Sort result for comparison
        result = [sorted(group) for group in result]
        result.sort()
        expected = [sorted(["a", "a"]), sorted(["b", "b"]), sorted(["c"])]
        expected.sort()
        self.assertEqual(result, expected, "Should group single character strings correctly")
    
    def test_different_length_strings(self):
        strs = ["a", "ab", "ba", "abc"]
        result = self.solution.groupAnagrams(strs)
        # Sort result for comparison
        result = [sorted(group) for group in result]
        result.sort()
        expected = [sorted(["a"]), sorted(["ab", "ba"]), sorted(["abc"])]
        expected.sort()
        self.assertEqual(result, expected, "Should handle strings of different lengths")
    
    def test_duplicate_words(self):
        strs = ["listen", "silent", "listen"]
        result = self.solution.groupAnagrams(strs)
        # Sort result for comparison
        result = [sorted(group) for group in result]
        self.assertEqual(len(result), 1, "Should have one group")
        self.assertEqual(sorted(result[0]), sorted(["listen", "silent", "listen"]), "Should include duplicates in same group")
    
    def test_large_input(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = self.solution.groupAnagrams(strs)
        # Sort result for comparison
        result = [sorted(group) for group in result]
        result.sort()
        expected = [sorted(["bat"]), sorted(["eat", "tea", "ate"]), sorted(["tan", "nat"])]
        expected.sort()
        self.assertEqual(result, expected, "Should handle larger input correctly")

# Custom Test Runner
class CustomTestRunner(unittest.TextTestRunner):
    def run(self, test):
        result = super().run(test)
        if result.wasSuccessful():
            print("\nAll tests passed successfully!")
        return result

# Run tests when the file is executed directly
if __name__ == "__main__":
    unittest.main(testRunner=CustomTestRunner())
