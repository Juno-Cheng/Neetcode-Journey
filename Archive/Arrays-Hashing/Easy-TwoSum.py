#https://leetcode.com/problems/two-sum/description/

#Default Libraries -------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

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
    def twoSum(self, nums, target):
        hashMap = {}
        for index, value in enumerate(nums):
            if target - value in hashMap:
                return [hashMap[target - value],index]
            hashMap[value] = index

'''
By going => in the nums list, we are searching each number and reminder. If it doesn't exist, we save the values in the Hashmap.
[0,1,2,2], 4

Therefore, we can also handle duplicates, since it will be moving in 1 directions, 
and the current index will always be in front of the hashmap value, if found.

'''