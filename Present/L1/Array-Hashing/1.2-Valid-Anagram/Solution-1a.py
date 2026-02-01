#https://leetcode.com/problems/contains-duplicate/description/
'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false

Constraints:
s and t consist of lowercase English letters.

Recommended Time & Space Complexity
You should aim for a solution with O(n + m) time and O(1) space, where n is the length of the string s and m is the length of the string t.

Topics:
- Arrays
- Hashing
- Strings
'''
#Default Libraries ------------- Try to get 99% Percentile Time/Space
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import unittest

'''
======================================
Basic Restrictions: 
No built-in functions (e.g., Counter, sorted)
No using built-in string methods for comparison

Algorithmic Restrictions
No Sorting: You cannot sort the strings to compare them.
Hash Map Approach: Use dictionaries to count character frequencies in both strings.
Two-Pass Solution: Iterate through each string once to build frequency maps, then compare.

Language/Implementation Restrictions
Dictionary Operations: Use dictionary.get() method to safely access and update character counts.
Dictionary Comparison: Compare the two frequency dictionaries using == operator.

Hard Mode
Single Pass: Solve the problem in a single traversal by incrementing counts for one string and decrementing for the other.
Constant Space: Use a fixed-size array (26 elements for lowercase letters) instead of a dictionary.
No Dictionary Comparison: Manually compare character frequencies without using == on dictionaries.

======================================
Thought Process:
- Hash Map Approach
Use two dictionaries to count character frequencies in both strings s and t.
Compare the dictionaries to check if they contain the same characters with the same frequencies.
Time Complexity - O(n + m) where n is length of s and m is length of t
Space Complexity - O(k) where k is the number of unique characters (at most 26 for lowercase letters)
'''

class Solution: # Built-In
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict, t_dict = {}, {}
        for let in s:
            s_dict[let] = s_dict.get(let, 0) + 1
        for let in t:
            t_dict[let] = t_dict.get(let, 0) + 1

        return s_dict == t_dict

# Test Cases ======================================
class UnitTest(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Solution class for testing
        self.solution = Solution()
    
    def test_valid_anagram(self):
        s, t = "racecar", "carrace"
        self.assertTrue(self.solution.isAnagram(s, t), "Should return True for valid anagrams")
    
    def test_not_anagram(self):
        s, t = "jar", "jam"
        self.assertFalse(self.solution.isAnagram(s, t), "Should return False when strings are not anagrams")
    
    def test_empty_strings(self):
        s, t = "", ""
        self.assertTrue(self.solution.isAnagram(s, t), "Should return True for empty strings")
    
    def test_single_character_same(self):
        s, t = "a", "a"
        self.assertTrue(self.solution.isAnagram(s, t), "Should return True for same single character")
    
    def test_single_character_different(self):
        s, t = "a", "b"
        self.assertFalse(self.solution.isAnagram(s, t), "Should return False for different single characters")
    
    def test_different_lengths(self):
        s, t = "abc", "ab"
        self.assertFalse(self.solution.isAnagram(s, t), "Should return False when strings have different lengths")
    
    def test_same_characters_different_counts(self):
        s, t = "aabb", "abab"
        self.assertTrue(self.solution.isAnagram(s, t), "Should return True when same characters with same counts")
    
    def test_different_counts(self):
        s, t = "aabb", "ab"
        self.assertFalse(self.solution.isAnagram(s, t), "Should return False when character counts differ")
    
    def test_all_same_character(self):
        s, t = "aaaa", "aaaa"
        self.assertTrue(self.solution.isAnagram(s, t), "Should return True when all characters are identical")
    
    def test_large_input_anagrams(self):
        s = "abcdefghijklmnopqrstuvwxyz" * 100
        t = "zyxwvutsrqponmlkjihgfedcba" * 100
        self.assertTrue(self.solution.isAnagram(s, t), "Should return True for large anagram inputs")

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
