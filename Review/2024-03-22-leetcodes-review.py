"""
LeetCode Review Notes
Date: 2024-03-22

This file contains review notes and solutions for LeetCode problems.
"""


#217. Contains Duplicate
'''Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
class Solution(object):
    def containsDuplicate1(self, nums):
        if len(set(nums)) == len(nums):
            return False
        return True
    
    def containsDuplicate2(self, nums):
        dupe = []
        for value in nums:
            if value in dupe:
                return True
            dupe.append(value)
        return False
    
    def containsDuplicate3(self, nums):
        hashMap = {}
        for value in nums:
            hashMap[value] = hashMap.get(value, 0) + 1
            if hashMap[value] > 1:
                return True
        return False
    


