"""
LeetCode Review Notes
Date: 2024-03-27

This file contains review notes and solutions for LeetCode problems.
"""

#1. Two Sum
'''
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

class Solution(object):
    def twoSum1(self, nums, target):
        hashMap = {}
        for index, value in enumerate(nums):
                if target - value in hashMap:
                    return [hashMap[target - value],index]
                hashMap[value] = index

    def twoSum2(self, nums, target):
        l=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    l.append(i)
                    l.append(j)
                    break
            if(len(l)>0):
                break        
        return l
        
    