#Default Libraries -------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
238. Product of Array Except Self
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


#Attempt 1 
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k = len(nums)
        lst = [1] * k
        left = 1
        for i in range(1,k):
            left *= nums[i-1]
            lst[i] = left
        
        right = 1
        for i in range(k-2, -1, -1):
            right *= nums[i+1]
            lst[i] *= right

        return lst

