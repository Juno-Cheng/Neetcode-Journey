#https://leetcode.com/problems/contains-duplicate/description/
'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
What does that mean for smaller index first?

Example 1:
Input: nums = [3,4,5,6], target = 7
Output: [0,1]

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]

Constraints:
2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
Only one valid answer exists.

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.
Topics:
- Arrays
- Hash Table
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
Built-In Functions Allowed: Use Python's built-in dictionary operations (in, assignment).
Data Structures Allowed: Dictionaries/hash maps are permitted for storing value-index pairs.

Algorithmic Restrictions
No Sorting: You cannot sort the array to find the pair (must preserve original indices).
Single Pass: Solve the problem in a single traversal of the array (O(n) time complexity).
Hash Map Approach: Use a dictionary to store values and their indices as you iterate.

Language/Implementation Restrictions
Dictionary Operations: Use 'in' operator to check if complement exists, and dictionary assignment to store values.
Index Tracking: Store each number's index in the dictionary as you encounter it.
Complement Calculation: Calculate target - current_number to find the needed complement.

Hard Mode
No Built-In Dictionary: Implement hash map functionality manually.
Two-Pass: First pass to build the dictionary, second pass to find the pair.
Nested Loops: Use nested loops to check all pairs (O(n²) time, O(1) space).
No Early Exit: Complete full iteration even after finding the pair.

======================================
Thought Process:
- Hash Map with Single Pass
Use a dictionary to store each number and its index as we iterate through the array. For each 
number, calculate the complement (target - current_number). Check if the complement exists in 
the dictionary and ensure it's not the same index (to avoid using the same element twice). 
If found, return the indices with the smaller index first. This approach allows us to find 
the solution in a single pass.
Time Complexity - O(n) where n is the length of the array (single traversal)
Space Complexity - O(n) where n is the number of unique values stored in the dictionary
'''

class Solution: # Built-In
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Use a Dict to store value we saw and store the index, we just need to loop once - O(n) and O(n) space
        dict, i = {}, 0
        for num in nums:
            if num not in dict:
                dict[num] = i
            reminder = int(target-num)
            if reminder in dict and dict[reminder] != i:
                return [dict[reminder],i]
            
            i += 1
        
        

# Test Cases ======================================
class UnitTest(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Solution class for testing
        self.solution = Solution()
    
    def test_basic_example_1(self):
        nums, target = [3, 4, 5, 6], 7
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 1], "Should return [0, 1] for nums[0] + nums[1] = 3 + 4 = 7")
    
    def test_basic_example_2(self):
        nums, target = [4, 5, 6], 10
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 2], "Should return [0, 2] for nums[0] + nums[2] = 4 + 6 = 10")
    
    def test_negative_numbers(self):
        nums, target = [-1, -2, -3, -4, -5], -8
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [2, 4], "Should handle negative numbers correctly")
    
    def test_mixed_positive_negative(self):
        nums, target = [2, 7, 11, -3], 8
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 3], "Should handle mixed positive and negative numbers")
    
    def test_duplicate_values(self):
        nums, target = [3, 3], 6
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 1], "Should handle duplicate values at different indices")
    
    def test_zero_in_array(self):
        nums, target = [0, 4, 3, 0], 0
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 3], "Should handle zero values correctly")
    
    def test_large_numbers(self):
        nums, target = [1000000, 2000000, 3000000], 3000000
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 2], "Should handle large numbers")
    
    def test_smallest_valid_array(self):
        nums, target = [2, 7], 9
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 1], "Should work with array of size 2")
    
    def test_not_at_beginning(self):
        nums, target = [1, 2, 3, 4, 5], 9
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [3, 4], "Should find pairs not at the beginning")
    
    def test_smaller_index_first(self):
        nums, target = [1, 5, 3, 2], 4
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), result, "Should return indices with smaller index first")
        self.assertEqual(result, [0, 2], "Should return [0, 2] for 1 + 3 = 4")
    
    def test_target_zero(self):
        nums, target = [-1, 0, 1, 2], 0
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 2], "Should return [0, 2] for -1 + 1 = 0")
    
    def test_same_number_different_indices(self):
        nums, target = [2, 5, 5, 11], 10
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [1, 2], "Should return [1, 2] for two 5s at different indices")

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
