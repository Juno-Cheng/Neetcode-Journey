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

Naive Solution - Three Separate Checks:

1. Check Each Row:
   - Iterate through each row in the board
   - Use a hash map to track frequency of each digit (1-9)
   - If any digit appears more than once (and it's not '.'), return False
   - Time: O(9) per row × 9 rows = O(81) = O(1) since board is fixed size
   - Space: O(9) = O(1) for hash map per row

2. Check Each Column:
   - Iterate through each column index (0-8)
   - For each column, iterate through all rows to access column values
   - Use board[j][i] where j is row index and i is column index
   - Use a hash map to track frequency of each digit
   - If any digit appears more than once (and it's not '.'), return False
   - Time: O(9) per column × 9 columns = O(81) = O(1)
   - Space: O(9) = O(1) for hash map per column

3. Check Each 3x3 Grid:
   - There are 9 sub-boxes: iterate through box starting positions (0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)
   - For each box, iterate through the 3×3 = 9 cells within that box
   - Use a hash map to track frequency of each digit
   - If any digit appears more than once (and it's not '.'), return False
   - Time: O(9) per box × 9 boxes = O(81) = O(1)
   - Space: O(9) = O(1) for hash map per box

Overall Time Complexity: O(1) 
- Since the board is always 9×9, we have a constant number of operations
- Alternatively, O(n²) where n=9, but since n is constant, it's effectively O(1)

Overall Space Complexity: O(1)
- We use hash maps with at most 9 entries each
- The space doesn't grow with input size since board is fixed

Optimization Opportunities:
- Can combine all three checks into a single pass using string keys like "row-0-5", "col-3-7", "box-1-2-9"
- Use sets instead of hash maps if we only need to check existence (not frequency)
- Early exit: return False immediately when duplicate is found (already implemented)

'''

class Solution: # Built-In
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check Each Row
        for row in board:
            hashMap = {}
            for i in row:
                hashMap[i] = hashMap.get(i, 0) + 1 
                if i != '.' and hashMap[i] != 1:
                    return False

        # Check Each Column
        for i in range(len(board)):
            hashMap = {}
            for j in range(len(board)):  # j = row index
                hashMap[board[j][i]] = hashMap.get(board[j][i], 0) + 1  # board[row][column] = board[j][i]
                if board[j][i] != '.' and hashMap[board[j][i]] != 1:
                    return False


        # Check each 3x3 Gridce
        # Time Complexity: O(1) - NOT O(N^4) because:
        # - Loop 1 (i): 3 iterations (0, 3, 6) - step size is 3, not 1
        # - Loop 2 (j): 3 iterations per i = 3 × 3 = 9 total
        # - Loop 3 (k): 3 iterations per (i,j) - always exactly 3 (i+3 - i = 3)
        # - Loop 4 (l): 3 iterations per (i,j,k) - always exactly 3 (j+3 - j = 3)
        # Total: 3 × 3 × 3 × 3 = 81 operations (CONSTANT, not dependent on N)
        # All loop bounds are constants (9, 3), so it's O(1), not O(N^4)cause we are still checking a total of 81
        for i in range(0, 9, 3):        # 3 iterations: i = 0, 3, 6
            for j in range(0, 9, 3):    # 3 iterations per i: j = 0, 3, 6
                hashMap = {}
                for k in range(i, i+3): # 3 iterations: k = i, i+1, i+2
                    for l in range(j, j+3): # 3 iterations: l = j, j+1, j+2
                        hashMap[board[k][l]] = hashMap.get(board[k][l], 0) + 1
                        if board[k][l] != '.' and hashMap[board[k][l]] != 1:
                            return False
        
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
