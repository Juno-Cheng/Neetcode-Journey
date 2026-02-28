"""
LeetCode Review Notes
Date: 2026-02-27

This file contains review notes and solutions for LeetCode problems from L1: Array-Hashing.
"""

# ============================================================================
# 1.1 Contains Duplicate
# ============================================================================
"""
Question:
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Examples:
Input: nums = [1, 2, 3, 3]
Output: true

Input: nums = [1, 2, 3, 4]
Output: false

Topics:
- Arrays
- Hash Table
- Sorting

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution1_1:
    def hasDuplicate(self, nums) -> bool:
        # TODO: Implement Solution 1
        pass
    
    def hasDuplicate2(self, nums) -> bool:
        # TODO: Implement Solution 2
        pass
    
    def hasDuplicate3(self, nums) -> bool:
        # TODO: Implement Solution 3
        pass


# ============================================================================
# 1.2 Valid Anagram
# ============================================================================
"""
Question:
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Examples:
Input: s = "racecar", t = "carrace"
Output: true

Input: s = "jar", t = "jam"
Output: false

Topics:
- Arrays
- Hashing
- Strings

Time Complexity: O(n + m)
Space Complexity: O(1) - at most 26 characters
"""

class Solution1_2:
    def isAnagram(self, s: str, t: str) -> bool:
        # TODO: Implement Solution 1
        pass
    
    def isAnagram2(self, s: str, t: str) -> bool:
        # TODO: Implement Solution 2
        pass
    
    def isAnagram3(self, s: str, t: str) -> bool:
        # TODO: Implement Solution 3
        pass


# ============================================================================
# 1.3 Two Sum
# ============================================================================
"""
Question:
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Examples:
Input: nums = [3,4,5,6], target = 7
Output: [0,1]

Input: nums = [4,5,6], target = 10
Output: [0,2]

Topics:
- Arrays
- Hash Table

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution1_3:
    def twoSum(self, nums, target: int):
        # TODO: Implement Solution 1
        pass
    
    def twoSum2(self, nums, target: int):
        # TODO: Implement Solution 2
        pass
    
    def twoSum3(self, nums, target: int):
        # TODO: Implement Solution 3
        pass


# ============================================================================
# 1.4 Group Anagrams
# ============================================================================
"""
Question:
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Examples:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Input: strs = ["x"]
Output: [["x"]]

Topics:
- Arrays
- Hash Table
- Sorting
- Strings

Time Complexity: O(m * n log n) where m is number of strings, n is average length
Space Complexity: O(m * n)
"""

class Solution1_4:
    def groupAnagrams(self, strs):
        # TODO: Implement Solution 1
        pass
    
    def groupAnagrams2(self, strs):
        # TODO: Implement Solution 2
        pass


# ============================================================================
# 1.5 Top K Frequent Elements
# ============================================================================
"""
Question:
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Examples:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Input: nums = [7,7], k = 1
Output: [7]

Topics:
- Arrays
- Hash Table
- Sorting
- Heap
- Bucket Sort
- Quick Select

Time Complexity: O(n log n) with sorting, O(n) with bucket sort
Space Complexity: O(n)
"""

class Solution1_5:
    def topKFrequent(self, nums, k: int):
        # TODO: Implement Solution 1
        pass
    
    def topKFrequent2(self, nums, k: int):
        # TODO: Implement Solution 2
        pass
    
    def topKFrequent3(self, nums, k: int):
        # TODO: Implement Solution 3
        pass


# ============================================================================
# 1.6 Encode and Decode Strings
# ============================================================================
"""
Question:
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.

Examples:
Input: strs = ["neet","code","love","you"]
Output: "4#neet4#code4#love3#you"

Topics:
- Arrays
- String
- Design

Time Complexity: O(n) where n is total characters
Space Complexity: O(n)
"""

class Solution1_6:
    def encode(self, strs):
        # TODO: Implement encode
        pass
    
    def decode(self, s):
        # TODO: Implement decode
        pass


# ============================================================================
# 1.7 Product of Array Except Self
# ============================================================================
"""
Question:
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.

Examples:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

Topics:
- Arrays
- Prefix Sum

Time Complexity: O(n)
Space Complexity: O(1) excluding output array
"""

class Solution1_7:
    def productExceptSelf(self, nums):
        # TODO: Implement Solution 1
        pass
    
    def productExceptSelf2(self, nums):
        # TODO: Implement Solution 2
        pass


# ============================================================================
# 1.8 Valid Sudoku
# ============================================================================
"""
Question:
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
- Each row must contain the digits 1-9 without duplicates.
- Each column must contain the digits 1-9 without duplicates.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

Examples:
Input: board = [["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]]
Output: true

Topics:
- Arrays
- Hash Table
- Matrix

Time Complexity: O(1) - fixed 9x9 board
Space Complexity: O(1)
"""

class Solution1_8:
    def isValidSudoku(self, board):
        # TODO: Implement solution
        pass


# ============================================================================
# 1.9 Longest Consecutive Sequence
# ============================================================================
"""
Question:
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
The elements do not have to be consecutive in the original array.
You must write an algorithm that runs in O(n) time.

Examples:
Input: nums = [2,20,4,10,3,4,5]
Output: 4  # [2,3,4,5]

Input: nums = [0,3,2,5,4,6,1,1]
Output: 7  # [0,1,2,3,4,5,6]

Topics:
- Arrays
- Hash Table
- Union Find

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution1_9:
    def longestConsecutive(self, nums):
        # TODO: Implement Solution 1
        pass
    
    def longestConsecutive2(self, nums):
        # TODO: Implement Solution 2
        pass


# ============================================================================
# Run Unit Tests
# ============================================================================
if __name__ == "__main__":
    import sys
    import os
    
    # Add the UnitTests directory to path
    unit_tests_dir = os.path.join(os.path.dirname(__file__), 'UnitTests')
    sys.path.insert(0, unit_tests_dir)
    
    # Import and run unit tests
    try:
        from L1 import run_all_tests
        print("\n" + "="*70)
        print("Running Unit Tests for L1: Array-Hashing")
        print("="*70 + "\n")
        run_all_tests()
    except ImportError as e:
        print(f"Error importing unit tests: {e}")
        print("Make sure Review/UnitTests/L1.py exists")
