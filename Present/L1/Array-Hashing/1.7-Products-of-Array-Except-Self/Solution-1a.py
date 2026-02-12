#https://leetcode.com/problems/product-of-array-except-self/description/
'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

Constraints:
2 <= nums.length <= 1000
-20 <= nums[i] <= 20

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.

Topics:
- Arrays
- Prefix Sum

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
Built-In Functions Allowed: Basic arithmetic operations, list operations, and range() are permitted.
Data Structures Allowed: Arrays/lists are permitted for storing prefix and suffix products.

Algorithmic Restrictions
Division Operation: The follow-up requires solving without using the division operation.
Two Pass Approach: You can use two passes through the array (forward and backward) to calculate products.
Prefix/Suffix Products: Use prefix products from left and suffix products from right to build the result.

Language/Implementation Restrictions
Single Array Output: Return a single array where each element is the product of all other elements.
In-Place Modification: You can modify the output array in-place during the second pass.
Constant Space (Follow-up): The optimal solution uses O(1) extra space (excluding the output array).

Hard Mode
No Extra Space: Solve using only the output array for intermediate calculations (O(1) extra space).
No Division: Cannot use division to calculate products (must use prefix/suffix approach).
Single Pass: Attempt to minimize the number of passes through the array.

======================================
Thought Process:
Lets go for the naive solution first:
- This is a O(n^2) time and O(n) space solution.
- We store a return array of the same length as the input array.

- We loop through the array and for each element, we loop through the array again and multiply the elements together except for the current element.
'''

class Solution: # Built-In
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        returnArr = [0] * len(nums)
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            
            returnArr[i] = product
        
        return returnArr



# Test Cases ======================================
class UnitTest(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Solution class for testing
        self.solution = Solution()
    
    def test_basic_example_1(self):
        nums = [1, 2, 4, 6]
        result = self.solution.productExceptSelf(nums)
        expected = [48, 24, 12, 8]
        self.assertEqual(result, expected, "Should return product of all elements except self")
    
    def test_basic_example_2(self):
        nums = [-1, 0, 1, 2, 3]
        result = self.solution.productExceptSelf(nums)
        expected = [0, -6, 0, 0, 0]
        self.assertEqual(result, expected, "Should handle arrays with zeros correctly")
    
    def test_minimum_length(self):
        nums = [2, 3]
        result = self.solution.productExceptSelf(nums)
        expected = [3, 2]
        self.assertEqual(result, expected, "Should handle minimum array length of 2")
    
    def test_all_positive_numbers(self):
        nums = [1, 2, 3, 4]
        result = self.solution.productExceptSelf(nums)
        expected = [24, 12, 8, 6]
        self.assertEqual(result, expected, "Should handle all positive numbers")
    
    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4]
        result = self.solution.productExceptSelf(nums)
        expected = [-24, -12, -8, -6]
        self.assertEqual(result, expected, "Should handle all negative numbers")
    
    def test_mixed_positive_negative(self):
        nums = [-1, 2, -3, 4]
        result = self.solution.productExceptSelf(nums)
        expected = [-24, 12, -8, 6]
        self.assertEqual(result, expected, "Should handle mixed positive and negative numbers")
    
    def test_single_zero(self):
        nums = [1, 0, 3, 4]
        result = self.solution.productExceptSelf(nums)
        expected = [0, 12, 0, 0]
        self.assertEqual(result, expected, "Should handle single zero in array")
    
    def test_multiple_zeros(self):
        nums = [0, 0, 2, 3]
        result = self.solution.productExceptSelf(nums)
        expected = [0, 0, 0, 0]
        self.assertEqual(result, expected, "Should handle multiple zeros in array")
    
    def test_with_ones(self):
        nums = [1, 1, 1, 1]
        result = self.solution.productExceptSelf(nums)
        expected = [1, 1, 1, 1]
        self.assertEqual(result, expected, "Should handle array of ones")
    
    def test_large_input(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = self.solution.productExceptSelf(nums)
        # Calculate expected manually: for index 0, product of 2*3*4*5*6*7*8*9*10 = 3628800
        expected = [3628800, 1814400, 1209600, 907200, 725760, 604800, 518400, 453600, 403200, 362880]
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
