"""
LeetCode Review Notes
Date: 2024-05-23

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

class Solution:
    def hasDuplicate1(self, nums: List[int]) -> bool:
        return len(nums) == len(set(nums))
    
    def hasDuplicate2(self, nums: List[int]) -> bool: 
        for i in set(nums):
              if nums.count(nums) != 1:
                   return False
        return True
    
    def hasDuplicate3(self, nums: List[int]) -> bool:
        hashMap = {}
        for i in nums:
            hashMap[i] = hashMap.get(i,0) + 1
            if hashMap[i] > 1:
                return False
        return True


 