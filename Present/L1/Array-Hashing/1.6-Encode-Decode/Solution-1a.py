#https://leetcode.com/problems/top-k-frequent-elements/description/
'''
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
    // ... your code
    return encoded_string;
}
Machine 2 (receiver) has the function:

vector<string> decode(string s) {
    //... your code
    return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.


===================================================

Example 1:
Input: dummy_input = ["Hello","World"]

Output: ["Hello","World"]

Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);


Example 2:
Input: dummy_input = [""]

Output: [""]

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.


Topics:
- Arrays
- String
- Design
- Sequencing


'''
#Default Libraries ------------- Try to get 99% Percentile Time/Space
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import unittest
from typing import List

'''
======================================
Basic Restrictions: 
Built-In Functions Allowed: Use Python's built-in sorted() function and dictionary operations.
Data Structures Allowed: Dictionaries/hash maps are permitted for grouping anagrams.

Algorithmic Restrictions
Sorting Allowed: You can sort strings to create keys for grouping anagrams.
Hash Map Approach: Use a dictionary where keys are sorted character strings and values are lists of anagrams.
Single Pass: Group all anagrams in a single traversal of the input array.

Language/Implementation Restrictions
String Sorting: Use sorted(string) to create a sorted character list, then join to create a hashable key.
Dictionary Grouping: Use dictionary.setdefault() or if/else to group strings by their sorted character key.
List Return: Return all groups (dictionary values) as a list of lists.

Hard Mode
No Built-In Sort: Implement character counting using arrays or dictionaries instead of sorting.
Character Counting: Use ord() to count character frequencies with a fixed-size array (26 for lowercase).
Tuple Keys: Convert character count arrays to tuples for hashable dictionary keys.
No Dictionary: Use alternative data structures for grouping.

======================================
Thought Process:
This question is like the bioinformatics question where we need to sequence strings of DNA or RNA.
- It is also very similar to the encryption class where we used a RSA encryption algorithm.

In order to encode the strings, we need to use a delimiter to separate the strings in the encoded string.
- Ex. Like commands in a CSV Files, we need a Start and End delimiter to separate the commands.

Encode:

Decode:
- Go through the encoded string one by one, and when we encounter a delimiter, we add the string to the list.
'''

class Solution: # Built-In
    def encode(self, strs: List[str]) -> str:
        pass

    def decode(self, s: str) -> List[str]:
        pass
# Test Cases ======================================
class UnitTest(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Solution class for testing
        self.solution = Solution()
    
    def test_basic_example_1(self):
        nums, k = [1, 2, 2, 3, 3, 3], 2
        result = self.solution.topKFrequent(nums, k)
        # Sort result for comparison (order doesn't matter)
        result.sort()
        expected = [2, 3]
        expected.sort()
        self.assertEqual(result, expected, "Should return top 2 most frequent elements")
    
    def test_basic_example_2(self):
        nums, k = [7, 7], 1
        result = self.solution.topKFrequent(nums, k)
        self.assertEqual(result, [7], "Should return single most frequent element")
    
    def test_single_element(self):
        nums, k = [1], 1
        result = self.solution.topKFrequent(nums, k)
        self.assertEqual(result, [1], "Should handle single element")
    
    def test_all_same_elements(self):
        nums, k = [5, 5, 5, 5], 1
        result = self.solution.topKFrequent(nums, k)
        self.assertEqual(result, [5], "Should return element when all are same")
    
    def test_k_equals_distinct_count(self):
        nums, k = [1, 2, 3], 3
        result = self.solution.topKFrequent(nums, k)
        result.sort()
        expected = [1, 2, 3]
        expected.sort()
        self.assertEqual(result, expected, "Should return all elements when k equals distinct count")
    
    def test_negative_numbers(self):
        nums, k = [-1, -1, -2, -2, -2], 2
        result = self.solution.topKFrequent(nums, k)
        result.sort()
        expected = [-2, -1]
        expected.sort()
        self.assertEqual(result, expected, "Should handle negative numbers")
    
    def test_mixed_frequencies(self):
        nums, k = [1, 1, 1, 2, 2, 3], 2
        result = self.solution.topKFrequent(nums, k)
        result.sort()
        expected = [1, 2]
        expected.sort()
        self.assertEqual(result, expected, "Should return top k elements with different frequencies")
    
    def test_large_input(self):
        nums = [1] * 100 + [2] * 50 + [3] * 25
        k = 2
        result = self.solution.topKFrequent(nums, k)
        result.sort()
        expected = [1, 2]
        expected.sort()
        self.assertEqual(result, expected, "Should handle large input correctly")

# Custom Test Runner
class CustomTestRunner(unittest.TextTestRunner):
    def run(self, test):
        result = super().run(test)
        if result.wasSuccessful():
            print("\nAll tests passed successfully!")
        return result

# Run tests when the file is executed directly
if __name__ == "__main__":
    unittest.main(testRunner=CustomTestRunner())
