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
Built-In Functions Allowed: Use Python's built-in set() operations (add, in operator).
Data Structures Allowed: Sets are permitted for tracking seen elements.

Algorithmic Restrictions
No Sorting: You cannot sort the array to find duplicates.
Single Pass with Early Exit: Iterate through the array once, but return immediately when a duplicate is found.
Hash Set Approach: Use a set to track elements we've seen so far.

Language/Implementation Restrictions
Set Operations: Use set.add() to add elements and 'in' operator to check membership.
Early Exit: Return True immediately when a duplicate is detected (optimization).

Hard Mode
No Built-In Set: Implement set functionality manually using a dictionary/hash map.
Constant Space: Solve without using extra space (requires sorting or mathematical approach).
No Early Exit: Complete the full iteration even after finding a duplicate (less efficient).

======================================
Thought Process:
- Hash Set with Early Exit
Use a set to track elements as we iterate through the array. For each element, check if it's 
already in the set. If yes, return True immediately (early exit optimization). If no, add it to 
the set and continue. This approach is more efficient than Solution-1a when duplicates appear early.
Time Complexity - O(n) worst case, but O(k) average case where k is the position of first duplicate
Space Complexity - O(n) worst case, but O(k) average case where k is the number of unique elements before duplicate
'''

class Solution: # Built-In
    def hasDuplicate(self, nums) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)

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
