"""
LeetCode Review Notes
Date: 2024-04-05

This file contains review notes and solutions for LeetCode problems.
"""

#Product Expect Self
'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

class Solution(object):
    def productExceptSelf1(self, nums):
        n = len(nums)
        left, right, answer = [0]*n, [0]*n, [0]*n

        # Calculate left products
        left[0] = 1
        for i in range(1, n):
            left[i] = nums[i - 1] * left[i - 1]
        
        # Calculate right products
        right[n - 1] = 1
        for i in reversed(range(n - 1)):
            right[i] = nums[i + 1] * right[i + 1]
        
        # Calculate the product of elements except itself
        for i in range(n):
            answer[i] = left[i] * right[i]
        print(left)
        print(right)
        return answer
    
    def productExceptSelf2(self, nums):
        n = len(nums)
        # Initialize the answer array with 1's since the product of no numbers is 1
        answer = [1] * n

        # First pass to fill in the products of elements to the left of each element
        left_accum = 1
        for i in range(n):
            answer[i] = left_accum
            left_accum *= nums[i]

        # Second pass to multiply the products of elements to the right of each element
        right_accum = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_accum
            right_accum *= nums[i]

        return answer
    
nums = [1,2,3,4]
x = Solution()
print(x.productExceptSelf1(nums))

#================== Lambda Practice
'''
Problem: Transform to Dictionary
Given a list of tuples where each tuple contains a name followed by a score, use a lambda function to transform this list into a dictionary where each key is the name, and the value is the score multiplied by 10 if the score is below 5, and by 5 otherwise.

Example Input: [("Alice", 4), ("Bob", 6), ("Charlie", 2)]
Expected Output: {"Alice": 40, "Bob": 30, "Charlie": 20}

'''

