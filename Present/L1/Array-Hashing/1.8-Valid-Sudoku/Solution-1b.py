#https://leetcode.com/problems/product-of-array-except-self/description/
'''
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Example 1:
Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true

Example 2:
Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: false

-------------------------------------------------------------------------------------
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
from pandas.plotting import PlotAccessor
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
- How do we improve our current solution?
- We can combine all three checks into a single pass using string keys like "row-0-5", "col-3-7", "box-1-2-9"
- We can use sets instead of hash maps if we only need to check existence (not frequency)
- We can early exit: return False immediately when duplicate is found (already implemented)

Remove hashmap and use sets instead, just like we did in Contains Duplicate.

'''

class Solution: # Built-In
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashMapRow = {}
        hashMapColumn = {}
        hashMapGrid = {}

        # Check Each Column
        for i in range(len(board)): # i = column index
            for j in range(len(board)):  # j = row index
                # Check Row and add to Set 
                if board[i][j] == '.':
                    continue

                hashMapRow[i] = hashMapRow.get(i, set())
                if board[i][j] in hashMapRow[i]:
                    return False
                # Add to Set
                hashMapRow[i].add(board[i][j])
                
                hashMapColumn[j] = hashMapColumn.get(j, set())
                if board[i][j] in hashMapColumn[j]:
                    return False
                    # Add to Set
                hashMapColumn[j].add(board[i][j])
                
                # Check 3x3 Grid and add to Set use // to get the box index
                boxIndex = (i // 3) * 3 + (j // 3)
                hashMapGrid[boxIndex] = hashMapGrid.get(boxIndex, set())
                if board[i][j] in hashMapGrid[boxIndex]:
                    return False
                # Add to Set
                hashMapGrid[boxIndex].add(board[i][j])
        
        return True


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
