#Default Libraries -------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique. So no [1,1,2,2,3,3] - Top 2

'''


#Attempt 1 
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashMap = {}
        for value in nums:
            if value in hashMap:
                hashMap[value] += 1
            else:
                hashMap[value] = 1
        
        return sorted(hashMap, key=lambda x: hashMap[x], reverse=True)[0:k]

nums = [1,1,1,2,2,3]
k = 2
sol = Solution()
print(sol.topKFrequent(nums,k))