"""
LeetCode Review Notes
Date: 2024-03-28

This file contains review notes and solutions for LeetCode problems.
"""


#49. Group Anagrams
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

class Solution(object):
    def groupAnagrams(self, strs):
        hashMap, returnList = {},[]

        for i in strs:
            x = ''.join(sorted(i))
            if x in hashMap:
                hashMap[x].append(i)
            else:
                hashMap[x] = [i]
        
        for i in hashMap.values():
            returnList.append(i)
        return returnList
                        
            