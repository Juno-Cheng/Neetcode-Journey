#https://leetcode.com/problems/encode-and-decode-strings/description/
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
import unittest
from typing import List

'''
======================================
Basic Restrictions: 
Built-In Functions Allowed: Basic string operations (concatenation, slicing, length), integer conversion, and list operations are permitted.
Data Structures Allowed: Strings and lists are permitted for encoding and decoding.

Algorithmic Restrictions
Length-Prefix Encoding: Use length-prefix encoding where each string is encoded as "length#string".
Delimiter Design: Use a delimiter (like '#') that separates the length from the string content.
Single Pass Encoding: Encode all strings in a single pass through the input list.
Single Pass Decoding: Decode all strings in a single pass through the encoded string.

Language/Implementation Restrictions
String Encoding: Encode each string as "length#string" format.
String Decoding: Parse the encoded string by reading length, then extracting that many characters.
Handle Empty Strings: Ensure empty strings are correctly encoded and decoded (e.g., "0#").
Handle Special Characters: The encoding must work with any ASCII characters, including those that might conflict with delimiters.

Hard Mode
No Delimiter Conflicts: Ensure the delimiter choice doesn't conflict with string content (length-prefix solves this).
Minimal Encoding Overhead: Minimize the space used for encoding metadata.
Efficient Parsing: Parse multi-digit lengths correctly (e.g., "10#helloworld" not "1#0#helloworld").

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
        encoded_string = ""
        for word in strs:
            length = len(word)
            encoded_word = f"{length}#{word}"
            encoded_string += encoded_word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        index = 0
        beginRead = False
        length = ""
        while index != len(s):
            if beginRead == False:
                if s[index] == '#':
                    beginRead = True
                else:
                    length += s[index]
                index += 1
                
            else:
                decoded_list.append(s[index:index+int(length)])
                index += int(length)
                length = ""
                beginRead = False

        # Edge Case: Last string is 0# - We were expecting more after the # but there was nothing. Therefore we get BeginRead = True but no more characters to read.
        # This breaks the while loop, so we need to add the last string manually.
        if beginRead == True: #Meaning last string is 0#
            decoded_list.append(s[index-1:(index-1)+int(length)])
            index += int(length)
            length = ""
            beginRead = False

        return decoded_list

# Test Cases ======================================
class UnitTest(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Solution class for testing
        self.solution = Solution()
    
    def test_basic_example_1(self):
        strs = ["Hello", "World"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs, "Should encode and decode basic example correctly")
    
    def test_basic_example_2(self):
        strs = [""]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs, "Should handle empty string in list")
    
    def test_empty_list(self):
        strs = []
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs, "Should handle empty list")
    
    def test_single_string(self):
        strs = ["Hello"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs, "Should handle single string")
    
    def test_multiple_strings(self):
        strs = ["", "test", "hello", "world"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs, "Should handle multiple strings including empty string")
    
    def test_strings_with_special_characters(self):
        strs = ["Hello#World", "test#123", "abc"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs, "Should handle strings containing delimiter character")
    
    def test_long_strings(self):
        strs = ["a" * 100, "b" * 50, "c" * 25]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs, "Should handle long strings correctly")
    
    def test_mixed_length_strings(self):
        strs = ["", "a", "ab", "abc", "abcd"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs, "Should handle strings of varying lengths")
    
    def test_strings_with_numbers(self):
        strs = ["123", "456", "789"]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs, "Should handle numeric strings")
    
    def test_all_empty_strings(self):
        strs = ["", "", ""]
        encoded = self.solution.encode(strs)
        decoded = self.solution.decode(encoded)
        self.assertEqual(decoded, strs, "Should handle multiple empty strings")

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
