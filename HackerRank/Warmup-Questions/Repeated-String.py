"""
Question:
There is a string, s, of lowercase English letters that is repeated infinitely
many times. Given an integer, n, find and print the number of letter a's in
the first n letters of the infinite string.

Examples:
Input: s = "aba", n = 10
Output: 7
Explanation: The first 10 letters of the infinite string are abaabaabaa.
There are 7 occurrences of 'a'.

Input: s = "a", n = 1000000000000
Output: 1000000000000
Explanation: All of the first n letters are 'a'.

Input: s = "abcac", n = 10
Output: 4
Explanation: The first 10 letters are abcacabcac. There are 4 a's.

Topics:
- Strings
- Math / Arithmetic
- Counting

Time Complexity: O(|s|)
Space Complexity: O(1)
"""

"""
Pseudocode:
1. Have a count variable to keep track of the number of 'a's in the string
2. Loop through the string and count the number of 'a's
3. Multiply the count by the number of times the string is repeated
4. Add any remaining 'a's from the partial repeat
5. Return the count
==============================
In a previous version of the code, I used a loop to count the number of 'a's in the string. And having a counter to match n.
- This was inefficient because it was looping through the string multiple times. It took too long to run.
- Looping through 10^7 items takes around 10 seconds on my machine. However 10^12 takes around ~11.7 days/
- Use this information from constraints to optimize the code. 
"""
def repeatedString(s: str, n: int) -> int:
    # Initialize the count of 'a's in the string
    count = 0

    # Get the count of 'a's in the string
    for letter in s:
        if letter == 'a':
            count += 1
    
    # Multiply and Get Remainder
    count *= n // len(s) # Flat division get the max number of full repeats

    # Add any remaining 'a's from the partial repeat
    remainder = n % len(s)
    for letter in s[:remainder]:
        if letter == 'a':
            count += 1

    return count

if __name__ == "__main__":
    assert repeatedString("aba", 10) == 7  # sample 0
    assert repeatedString("a", 1000000000000) == 1000000000000  # sample 1
    assert repeatedString("abcac", 10) == 4
    assert repeatedString("abc", 0) == 0  # no characters to consider
    assert repeatedString("bcd", 100) == 0  # no a's in the string
    assert repeatedString("aaa", 5) == 5  # all a's, partial last repeat
    print("All tests passed.")
