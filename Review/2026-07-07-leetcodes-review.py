"""
LeetCode Review Notes
Date: 2026-07-07

This file contains review notes and solutions for LeetCode problems.

Max Consecutive Ones
You are given a binary array nums, return the maximum number of consecutive 1's in the array.

Input: nums = [1,1,0,1,1,1]

Output: 3
"""
class Solution:
    # Time Complexity: O(n), State Machine Pattern - Have a counter or state variable to track the current state of the problem.
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        counter, max = 0, 0 
        for x in nums:
            if str(x) == "1":
                counter += 1
            else: 
                if max < counter:
                    max = counter
                counter = 0
        if max < counter:
            max = counter
        return max
    
    # Time Complexity: O(n), Sliding Window Pattern - Have a window that slides across the array to find the maximum number of consecutive 1's.
    def findMaxConsecutiveOnes_SlidingWindow(self, nums: list[int]) -> int:
        left, right = 0, 0
        big = 0
        while right < len(nums):
            if nums[right] == 1:
                right += 1
            else:
                big = max(big, right - left)
                if right == len(nums):
                    break
                right += 1
                left = right
        if big < right - left:
            big = right - left
        return big
        
nums = [1,1,0,1,1,1]
sol = Solution()
print(sol.findMaxConsecutiveOnes(nums))
print(sol.findMaxConsecutiveOnes_SlidingWindow(nums))