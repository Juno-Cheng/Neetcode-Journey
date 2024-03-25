"""
LeetCode Review Notes
Date: 2024-03-24

This file contains review notes and solutions for LeetCode problems.
"""

#242. Valid Anagram
'''
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
'''

class Solution(object):
    def isAnagram1(self, s, t): #44 ms - Beats 16% - Very Sl
        if len(s) != len(t):
            return False
        if set(s) != set(t):
            return False
        
        x,y = sorted(s), sorted(t)
        return x == y

    def isAnagram2(self, s, t):
        if len(s) != len(t):
            return False
        if set(s) != set(t):
            return False
        
        x,y = sorted(s), sorted(t)
        return x == y
   
