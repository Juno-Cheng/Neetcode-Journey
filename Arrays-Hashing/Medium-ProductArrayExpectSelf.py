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
        count = len(nums)
        returnList = [1]*count

        #Left 
        for i in range(1,count):
            returnList[i] = nums[i-1] * returnList[i-1]

        #Right
        right = 1
        for i in range(count-1, -1, -1):
            returnList[i] *= right
            right *= nums[i] 
    
        return returnList