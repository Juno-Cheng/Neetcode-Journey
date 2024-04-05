"""
LeetCode Review Notes
Date: 2024-04-04

This file contains review notes and solutions for LeetCode problems.
"""


#347. Top K Frequent Elements
'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
'''


class Solution(object):
    def topKFrequent1(self, nums, k):
        hashMap = {}
        for i in nums:
            hashMap[i] = hashMap.get(i,0) + 1
        return sorted(hashMap, key=lambda x: hashMap[x], reverse=True)[:k]
    
    def topKFrequent2(self, nums, k):
        hashMap = {}
        for i in nums:
            hashMap[i] = hashMap.get(i,0) + 1
        return sorted(set(nums), key=lambda x: hashMap[x], reverse=True)[:k]


nums = [1,1,1,2,2,3]
k = 2

x = Solution()
print(x.topKFrequent1(nums,k))
print(x.topKFrequent2(nums,k))




