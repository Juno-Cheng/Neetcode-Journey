"""
Question:
There is a new mobile game that starts with consecutively numbered clouds.
Some of the clouds are thunderheads and others are cumulus. The player can
jump on any cumulus cloud having a number that is equal to the number of the
current cloud plus 1 or 2. The player must avoid the thunderheads. Determine
the minimum number of jumps it will take to jump from the starting position
to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered 0 if they are safe
or 1 if they must be avoided.

Examples:
Input: c = [0, 0, 1, 0, 0, 1, 0]
Output: 4
Explanation: Avoid indices 2 and 5. Path 0 -> 1 -> 3 -> 4 -> 6 takes 4 jumps
(path 0 -> 1 -> 3 -> 5 is invalid; 0 -> 2 is invalid). Minimum is 4.

Input: c = [0, 0, 0, 0, 1, 0]
Output: 3

Input: c = [0, 1, 0]
Output: 1

Topics:
- Arrays
- Greedy
- Jump Game / Sliding Window style traversal

Time Complexity: O(n)
Space Complexity: O(1)
"""


def jumpingOnClouds(c: list[int]) -> int:
    # Initialize the number of jumps and the current cloud
    jumps = 0
    current_cloud = 0

    # Loop till we reach the last cloud
    while current_cloud < len(c) - 1:
        # Check if the 2nd next cloud is safe
        if current_cloud + 2 < len(c) and c[current_cloud + 2] == 0:
            # Jump to the 2nd next cloud
            current_cloud += 2
        else:
            # Jump to the next cloud
            current_cloud += 1
        # Increment the jump count
        jumps += 1

    return jumps

"""
Pseudocode:
1. Have a variable to keep track of the number of jumps
2. Have a variable to keep track of the current cloud
3. Loop through the clouds
4. Check Cloud +2 is safe, if so, jump to it and increment the jump count
5. If Cloud +2 is not safe, jump to Cloud +1 and increment the jump count
6. Return the jump count

"""
if __name__ == "__main__":
    assert jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]) == 4  # sample 0
    assert jumpingOnClouds([0, 0, 0, 0, 1, 0]) == 3  # sample 1 style
    assert jumpingOnClouds([0, 0]) == 1  # shortest: one +1 jump
    assert jumpingOnClouds([0, 0, 0]) == 1  # one +2 jump
    assert jumpingOnClouds([0, 1, 0]) == 1  # must jump +2 over thunderhead
    print("All tests passed.")
