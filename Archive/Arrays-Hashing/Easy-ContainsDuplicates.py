#https://leetcode.com/problems/contains-duplicate/description/

#Default Libraries -------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


'''
Question:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

'''
#Solution:
class Solution(object):
    def containsDuplicate(self, nums):
        hashMap = {} #Hashmap Dict is created
        for i in nums: #For each value
            if i in hashMap: #If exist in Hashmap - Lookup O(1)
                return True
            hashMap[i] = 1
        return False
    
    def oneLiner(self,nums):
        hashMap = {}

#Other Solutions include using set/arrays or comparing values such as len(set) < len(num)
