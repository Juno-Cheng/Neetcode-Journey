"""
LeetCode Review Notes
Date: 2024-03-29

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
    def topKFrequent(self, nums, k):
        hashMap = {}
        for i in nums:
            hashMap[i] = hashMap.get(i,0) + 1
        
        return sorted(hashMap, key=lambda x: hashMap[x], reverse= True)[:k]

nums = [1,1,1,2,2,3]
k = 2
x = Solution()
print(x.topKFrequent(nums,k))


#================== Lambda Practice

'''
Problem 1: Double the Numbers
Given a list of numbers, use a lambda function with map() to double each number in the list.

Example Input: [1, 2, 3, 4]
Expected Output: [2, 4, 6, 8]
'''