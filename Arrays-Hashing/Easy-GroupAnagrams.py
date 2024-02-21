#Default Libraries -------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

'''


#Attempt 1 
class Solution(object):
    def groupAnagrams(self, strs):
        hashMap = {}
        for word in strs:
            x = ''.join(sorted(word)) 
            if x in hashMap:
                hashMap[x].append(word)
            else:
                hashMap[x] = [word]
        return [b for a,b in hashMap.items()]

solution = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams(strs))