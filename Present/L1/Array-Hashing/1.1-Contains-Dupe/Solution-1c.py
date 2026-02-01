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
Built-In Functions Allowed: Use Python's built-in sort() and len() functions.
Data Structures Allowed: Can modify the input array in-place.

Algorithmic Restrictions
Sorting Required: Sort the array first to group duplicates together.
Two-Pointer Technique: Use two pointers (p0, p1) to compare adjacent elements after sorting.
Single Pass After Sort: After sorting, traverse the sorted array once to find duplicates.

Language/Implementation Restrictions
In-Place Sorting: Use nums.sort() to sort the array in-place (modifies original array).
Pointer Comparison: Use two pointers to compare adjacent elements (nums[p0] == nums[p1]).
Edge Case Handling: Check for empty array before processing.

Hard Mode
No Built-In Sort: Implement your own sorting algorithm (merge sort, quicksort, etc.).
Constant Space: Use O(1) extra space (sorting still requires O(n) space for recursion stack or O(1) for iterative).
No Pointer Variables: Use array indexing directly without pointer variables.

======================================
Thought Process:
- Sort + Two Pointers
First sort the array to group duplicates together. Then use two pointers to traverse the sorted 
array, comparing adjacent elements. If any two adjacent elements are equal, a duplicate exists. 
This approach trades time complexity (O(n log n) due to sorting) for potentially better space 
complexity if sorting is done in-place, though Python's sort() uses O(n) space.
Time Complexity - O(n log n) due to sorting, then O(n) for traversal = O(n log n) overall
Space Complexity - O(n) for Python's Timsort algorithm
'''

class Solution: # Built-In
    def hasDuplicate(self, nums) -> bool:
        if len(nums) == 0:
            return False
        p0, p1 = 0, 1
        nums.sort()
        while p1 != len(nums):
            if nums[p0] == nums[p1]:
                return True
            p0 += 1
            p1 += 1
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
