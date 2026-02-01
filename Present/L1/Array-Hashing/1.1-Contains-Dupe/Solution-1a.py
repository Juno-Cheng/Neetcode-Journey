#https://leetcode.com/problems/contains-duplicate/description/
'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
'''
#Default Libraries ------------- Try to get 99% Percentile Time/Space
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import unittest

'''
======================================
Basic Restrictions: 
Built-In Functions Allowed: Use Python's built-in set() and len() functions.
Data Structures Allowed: Sets and dictionaries are permitted.

Algorithmic Restrictions
No Sorting: You cannot sort the array to find duplicates.
Set Conversion Approach: Convert the array to a set to automatically remove duplicates.
Length Comparison: Compare the length of the original array with the length of the set.

Language/Implementation Restrictions
Built-In Set: Use set() constructor to convert array to a set (removes duplicates automatically).
Length Comparison: Use len() and != operator to check if lengths differ (indicating duplicates exist).

Hard Mode
No Built-In Functions: Implement set functionality manually using a dictionary/hash map.
Single Pass with Early Exit: Use a hash set and return True immediately when a duplicate is found.
Constant Space: Solve without using extra space (requires sorting or mathematical approach).
Two-Pointer Technique: Use two pointers after sorting (requires sorting, so O(n log n) time).

======================================
Thought Process:
- Built-In Set Approach
Convert the array to a set, which automatically removes duplicates. If the set has fewer elements 
than the original array, duplicates exist. This is the simplest and most Pythonic solution.
Time Complexity - O(n) where n is the length of the array (set conversion iterates through all elements)
Space Complexity - O(n) where n is the number of unique elements (set stores unique values)
'''

class Solution: # Built-In
    def hasDuplicate(self, nums) -> bool:
        return len(set(nums)) != len(nums)

# Test Cases ======================================
class UnitTest(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Solution class for testing
        self.solution = Solution()
    
    def test_no_duplicates(self):
        nums = [1, 2, 3, 4, 5]
        self.assertFalse(self.solution.hasDuplicate(nums), "Should return False for no duplicates")
    
    def test_with_duplicates(self):
        nums = [1, 2, 3, 3]
        self.assertTrue(self.solution.hasDuplicate(nums), "Should return True for duplicates")
    
    def test_empty_list(self):
        nums = []
        self.assertFalse(self.solution.hasDuplicate(nums), "Should return False for an empty list")
    
    def test_single_element(self):
        nums = [42]
        self.assertFalse(self.solution.hasDuplicate(nums), "Should return False for a single-element list")
    
    def test_large_input_with_duplicates(self):
        nums = [i for i in range(10**6)] + [999999]
        self.assertTrue(self.solution.hasDuplicate(nums), "Should return True for a large input with duplicates")
    
    def test_large_input_without_duplicates(self):
        nums = [i for i in range(10**6)]
        self.assertFalse(self.solution.hasDuplicate(nums), "Should return False for a large input without duplicates")
    
    def test_all_identical_elements(self):
        nums = [7, 7, 7, 7]
        self.assertTrue(self.solution.hasDuplicate(nums), "Should return True when all elements are identical")

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
