#https://leetcode.com/problems/top-k-frequent-elements/description/
'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]

Constraints:
1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.


Topics:
- Arrays
- Hash Table
- Divide and Conquer
- Sorting
- Heap
- Bucket Sort
- Counting
- Quick Select


'''
#Default Libraries ------------- Try to get 99% Percentile Time/Space
import numpy as np
import pandas as pd
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
- The Hash Map Approach was the Naive Solution:
This is because, while it takes O(n) time to count the frequencies, it takes O(n log n) time to sort the dictionary items.
This is because the sorted() function is implemented using a variant of quicksort, which has a worst-case time complexity of O(n log n).

Now the question based on the constrainst says that it is O(n) time and O(n) space, where n is the size of the input array.
So we need to use a different approach.

We can use a hash map to count the frequencies of the elements in the array.
Then we can use a heap/priority queue to sort the elements by their frequencies, instead of sorting the dictionary items.
Then we can return the top k elements from the heap.



This is a O(n) time and O(n) space solution.

'''

import heapq

class Solution: # Built-In
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}
        heap = []
        
        # Count frequencies - O(n) time
        for num in nums:
            numDict[num] = numDict.get(num, 0) + 1
        
        # Push the elements into the heap - O(n log n) time
        '''
        for num, freq in numDict.items():
            heapq.heappush(heap, (-freq, num))
        '''

        #Actually We can Call on Heapify to Sort the Elements by their Frequencies in O(m) time. Where m is the number of unique elements in the array.
        heap = heapq.heapify(numDict.items())
        
        returnArray = [0] * k
        # Pop the top k elements from the heap - k log n time - Which is better than n log n time in 
        for i in range(k):
            returnArray[i] = heapq.heappop(heap)[1] # [1] is the number, [0] is the frequency
        
        return returnArray 

        # This is better than 1a because instead of O(n log n) time, we have O(k log n) time.

        

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
