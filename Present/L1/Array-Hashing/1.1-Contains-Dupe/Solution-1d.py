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
Built-In Functions Allowed: Use Python's built-in dictionary operations (get, assignment).
Data Structures Allowed: Dictionaries/hash maps are permitted for tracking element frequencies.

Algorithmic Restrictions
No Sorting: You cannot sort the array to find duplicates.
Single Pass with Frequency Tracking: Iterate through the array once, tracking frequency of each element.
Hash Map Approach: Use a dictionary to count occurrences of each element.

Language/Implementation Restrictions
Dictionary Operations: Use dict.get(key, default) to safely access and update counts.
Frequency Check: Check if frequency is already 1 before incrementing (indicates duplicate found).
Early Exit: Return True immediately when a duplicate is detected.

Hard Mode
No Built-In Dictionary: Implement hash map functionality manually.
Constant Space: Solve without using extra space (requires sorting or mathematical approach).
Count All Frequencies: Complete full iteration and count all frequencies, then check for any > 1.

======================================
Thought Process:
- Hash Map with Frequency Tracking
Use a dictionary to track the frequency of each element as we iterate. For each element, check if 
its frequency is already 1 (meaning we've seen it before). If yes, return True immediately. 
Otherwise, increment its count. This is similar to Solution-1b but uses frequency counting 
instead of just membership checking, which can be useful if you need frequency information.
Time Complexity - O(n) worst case, but O(k) average case where k is the position of first duplicate
Space Complexity - O(n) worst case, but O(k) average case where k is the number of unique elements before duplicate
'''

class Solution: # Built-In
    def hasDuplicate(self, nums) -> bool:
        nums_dict = {}
        for num in nums:
            if nums_dict.get(num,0) == 1:
                return True
            nums_dict[num] = nums_dict.get(num,0) +1
        return False

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
