#https://leetcode.com/problems/longest-consecutive-sequence/description/
'''
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7

-------------------------------------------------------------------------------------
Constraints:
0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9

Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.

Topics:
- Arrays
- Hash Table
- Union Find

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
Built-In Functions Allowed: Basic arithmetic operations, list operations, set operations, and range() are permitted.
Data Structures Allowed: Arrays/lists, sets, and hash maps/dictionaries are permitted for storing and tracking elements.

Algorithmic Restrictions
Sorting Approach: You can use sorting (O(n log n)) for a simpler solution, but the optimal solution should be O(n).
Hash Set Approach: The optimal solution uses a hash set to achieve O(n) time complexity by checking for sequence starts.
Single Pass: The optimal solution should minimize the number of passes through the array.

Language/Implementation Restrictions
Integer Output: Return a single integer representing the length of the longest consecutive sequence.
Duplicate Handling: Duplicate elements should be ignored (only count unique values in sequences).
Sequence Definition: A consecutive sequence means each element is exactly 1 greater than the previous element.

Hard Mode
O(n) Time: Solve in O(n) time complexity without sorting.
Hash Set Only: Use only hash sets/maps for tracking, no sorting allowed.
Single Pass: Minimize passes through the array (ideally one pass for building set, one for checking sequences).

======================================
Thought Process:

## Step 1: Naive Solution (Solution-1a)
- Sort the array: O(n log n)
- Iterate through sorted array and count consecutive sequences
- Time: O(n log n), Space: O(1)

## Step 2: Identifying the Bottleneck
- Sorting is O(n log n) - can we avoid it?
- We're checking every element, but do we need to?

## Step 3: The Key Insight - "Sequence Start Optimization"
**Problem:** If we check every element and expand sequences from each:
- For [1, 2, 3, 4, 5]:
  - Expand from 1 → visits 2, 3, 4, 5
  - Expand from 2 → visits 3, 4, 5 (REDUNDANT!)
  - Expand from 3 → visits 4, 5 (REDUNDANT!)
  - This leads to O(n²) worst case

**Solution:** Only expand from sequence starts!
- A sequence starts when `num - 1` is NOT in the set
- If `num - 1` exists, then `num` is NOT a start → skip it
- This ensures each element is visited at most once in while loops

## Step 4: Optimal Solution
- Use hash set for O(1) lookups: O(n) to build
- Iterate through set: O(n) iterations
- Only expand from sequence starts: O(n) total while loop iterations
- Time: O(n), Space: O(n)

## Pattern: "Only Process Sequence Starts"
- Filter before processing
- Use condition to identify entry points
- Avoid redundant work by skipping non-starts

## Why O(n) and not O(n²)?
Even though there's a nested while loop:
- While loop only runs for sequence starts (typically 1 per sequence)
- Each element is visited at most once in all while loops combined
- Total: n outer iterations + n inner iterations = O(n)
'''

class Solution:
   def longestConsecutive(self, nums: List[int]) -> int:
            cutNums = set(nums)
            maxLen = 0
            # O(n) time complexity
            for num in cutNums:
                # Check if the previous element exists so that it is not the start of the sequence
                if num - 1 not in cutNums:
                    length = 1
                    while num + length in cutNums:
                        length += 1
                    maxLen = max(maxLen, length)
            return maxLen

                
            
        
        


# Test Cases ======================================
class UnitTest(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Solution class for testing
        self.solution = Solution()
    
    def test_basic_example_1(self):
        nums = [2, 20, 4, 10, 3, 4, 5]
        result = self.solution.longestConsecutive(nums)
        expected = 4  # Sequence: 2, 3, 4, 5
        self.assertEqual(result, expected, "Should return length of longest consecutive sequence")
    
    def test_basic_example_2(self):
        nums = [0, 3, 2, 5, 4, 6, 1, 1]
        result = self.solution.longestConsecutive(nums)
        expected = 7  # Sequence: 0, 1, 2, 3, 4, 5, 6
        self.assertEqual(result, expected, "Should handle sequence starting from 0")
    
    def test_empty_array(self):
        nums = []
        result = self.solution.longestConsecutive(nums)
        expected = 0
        self.assertEqual(result, expected, "Should return 0 for empty array")
    
    def test_single_element(self):
        nums = [1]
        result = self.solution.longestConsecutive(nums)
        expected = 1
        self.assertEqual(result, expected, "Should return 1 for single element")
    
    def test_no_consecutive_sequence(self):
        nums = [1, 3, 5, 7, 9]
        result = self.solution.longestConsecutive(nums)
        expected = 1  # Each element is its own sequence
        self.assertEqual(result, expected, "Should return 1 when no consecutive sequence exists")
    
    def test_all_duplicates(self):
        nums = [5, 5, 5, 5, 5]
        result = self.solution.longestConsecutive(nums)
        expected = 1  # Only one unique element
        self.assertEqual(result, expected, "Should handle all duplicate elements")
    
    def test_negative_numbers(self):
        nums = [-3, -2, -1, 0, 1]
        result = self.solution.longestConsecutive(nums)
        expected = 5  # Sequence: -3, -2, -1, 0, 1
        self.assertEqual(result, expected, "Should handle negative numbers in sequence")
    
    def test_mixed_positive_negative(self):
        nums = [-1, 0, 1, 2, 3, 10, 11, 12]
        result = self.solution.longestConsecutive(nums)
        expected = 5  # Sequence: -1, 0, 1, 2, 3 (longer than 10, 11, 12)
        self.assertEqual(result, expected, "Should find longest sequence among multiple sequences")
    
    def test_sequence_at_end(self):
        nums = [100, 4, 200, 1, 3, 2]
        result = self.solution.longestConsecutive(nums)
        expected = 4  # Sequence: 1, 2, 3, 4
        self.assertEqual(result, expected, "Should find sequence not at the beginning")
    
    def test_large_gap(self):
        nums = [1, 2, 3, 100, 101, 102, 103, 104, 105]
        result = self.solution.longestConsecutive(nums)
        expected = 6  # Sequence: 100, 101, 102, 103, 104, 105 (length 6)
        self.assertEqual(result, expected, "Should find longest sequence with large gaps")
    
    def test_sequence_with_duplicates(self):
        nums = [1, 2, 2, 3, 3, 3, 4, 5]
        result = self.solution.longestConsecutive(nums)
        expected = 5  # Sequence: 1, 2, 3, 4, 5 (duplicates ignored)
        self.assertEqual(result, expected, "Should ignore duplicates when finding sequence")
    
    def test_single_sequence_entire_array(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = self.solution.longestConsecutive(nums)
        expected = 10
        self.assertEqual(result, expected, "Should handle entire array as one sequence")

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
