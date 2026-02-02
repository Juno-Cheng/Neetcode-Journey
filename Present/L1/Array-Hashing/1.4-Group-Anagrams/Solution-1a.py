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
Built-In Functions Allowed: Use Python's built-in sorted() function and dictionary operations.
Data Structures Allowed: Dictionaries/hash maps are permitted for grouping anagrams.

Algorithmic Restrictions
Sorting Allowed: You can sort strings to create keys for grouping anagrams.
Hash Map Approach: Use a dictionary where keys are sorted character strings and values are lists of anagrams.
Single Pass: Group all anagrams in a single traversal of the input array.

Language/Implementation Restrictions
String Sorting: Use sorted(string) to create a sorted character list, then join to create a hashable key.
Dictionary Grouping: Use dictionary.setdefault() or if/else to group strings by their sorted character key.
List Return: Return all groups (dictionary values) as a list of lists.

Hard Mode
No Built-In Sort: Implement character counting using arrays or dictionaries instead of sorting.
Character Counting: Use ord() to count character frequencies with a fixed-size array (26 for lowercase).
Tuple Keys: Convert character count arrays to tuples for hashable dictionary keys.
No Dictionary: Use alternative data structures for grouping.

======================================
Thought Process:
- Hash Map with Sorted String Keys
Use a dictionary where the key is the sorted version of each string (anagrams will have the same 
sorted key). For each string, sort its characters and join them to create a consistent key. Group 
all strings with the same key together. This approach leverages the fact that anagrams have 
identical character compositions when sorted.
Time Complexity - O(m * n log n) where m is number of strings and n is average string length (sorting each string)
Space Complexity - O(m * n) where m is number of strings and n is average string length (storing all strings)
'''

class Solution: # Built-In
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a dictionary to group anagrams by their sorted character key
        groups = {}
        for word in strs:
            # Sort characters and join to create a consistent key for anagrams
            key = ''.join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        return list(groups.values())
        

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
