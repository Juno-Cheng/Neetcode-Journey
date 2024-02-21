#https://leetcode.com/problems/valid-anagram/

#Default Libraries -------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

class Solution(object):
    def isAnagram(self, s, t):
        hashMap = {}
        hashMap2 = {}
        #S
        for i in s:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 0
        
        #t
        for i in t:
            if i in hashMap2:
                hashMap2[i] += 1
            else:
                hashMap2[i] = 0
        
        return hashMap == hashMap2



'''
Planning:

Since we need to check if s and t have the same amount of chars we can use hashmap to store everything. - O(n) + O(n)
or
We can sort the s and t and check. - O(n log n)

#Note to self, make sure to do easy checks such as length not the same:

if len(s) != len(t): return False
'''