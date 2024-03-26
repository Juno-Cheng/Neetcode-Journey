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
        
        hashMap1, hashMap2 = {},{}

        for i in range(0,len(s)):
            hashMap1[s[i]] = hashMap1.get(s[i], 0 ) + 1
            hashMap2[t[i]] = hashMap2.get(t[i], 0 ) + 1
        
        return hashMap1 == hashMap2
   
s = "anagram"
t = "nagaram"
x = Solution()
print(x.isAnagram2(s,t))
