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
No built-in functions 
No using Data Structures

Algorithmic Restrictions
No Sorting: You cannot sort the array to find duplicates.
Single Pass: You must solve the problem in a single traversal of the array (O(n) time complexity).
Constant Space: You cannot use any extra space beyond a few variables (O(1) space complexity).
Two-Pointer Technique: Restrict yourself to solving the problem using two pointers without creating additional arrays or data structures.

Language/Implementation Restrictions
No Built-in Comparisons: Avoid using comparison operators (e.g., ==, !=, <, >) for detecting duplicates.
Bit Manipulation Only: Solve the problem using bitwise operations.

Hard Mode
Write It Recursively: Solve the problem using recursion instead of iteration.
Simulate Set Operations: Implement a "virtual set" using mathematical or bitwise techniques.

======================================
Thought Process:
- No Built-In Functions
Since len, set, and sort are restricted, we can use a hashMap to check for duplicatres.
Time Complexity - O(n)
Space Complexity - O(n)
'''

class Solution: # No Pointer, Loop
    def hasDuplicate(self, nums) -> bool:
        nums.sort()
        for count in range(len(nums)-1):
            if nums[count] == nums[count+1]:
                return True
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
