# Array-Hashing

## Overview

This section covers fundamental array and hashing techniques essential for solving algorithmic problems.

## Topics

### Dynamic Arrays
**Data Structures & Algorithms for Beginners**

Dynamic arrays provide flexible storage that can grow or shrink as needed. Understanding their implementation and time complexity characteristics is crucial for efficient problem-solving.

**What are Dynamic Arrays?**
Dynamic arrays (like Python's `list`) automatically resize when elements are added or removed. Unlike static arrays with fixed size, dynamic arrays allocate more memory as needed.

**Key Characteristics:**
- **Amortized O(1) append**: Most appends are O(1), but occasionally O(n) when resizing
- **O(1) access by index**: Direct access to any element
- **O(n) insertion/deletion in middle**: Requires shifting elements

**Example:**
```python
# Python list is a dynamic array
arr = [1, 2, 3]
arr.append(4)        # O(1) amortized
arr.insert(0, 0)     # O(n) - shifts all elements
arr[2]               # O(1) - direct access
```

**When to Use:**
- When you need flexible size and frequent appends
- When you need random access by index
- When order matters and you need to maintain sequence

---

### Hash Usage
**Data Structures & Algorithms for Beginners**

Hash tables enable O(1) average-case lookups, insertions, and deletions. Learning when and how to use hash maps and hash sets is fundamental for optimizing solutions.

**What are Hash Tables?**
Hash tables (dictionaries in Python, `dict`) store key-value pairs using a hash function to map keys to array indices. This allows fast lookups without iterating through all elements.

**Key Characteristics:**
- **O(1) average-case** operations: insert, lookup, delete
- **O(n) worst-case**: When many collisions occur
- **No guaranteed order**: Keys are unordered (Python 3.7+ maintains insertion order)

**Example:**
```python
# Hash map (dictionary)
freq = {}
freq['apple'] = 5        # O(1) insert
freq['banana'] = 3       # O(1) insert
count = freq['apple']    # O(1) lookup
'apple' in freq          # O(1) check existence

# Hash set
seen = set()
seen.add(1)              # O(1) insert
1 in seen                # O(1) check existence
```

**Common Use Cases:**
- **Frequency counting**: Count occurrences of elements
- **Fast lookups**: Check if element exists
- **Grouping**: Group elements by a key
- **Caching**: Store computed results (memoization)

**Example Problem - Two Sum:**
```python
# Find two numbers that add up to target
def twoSum(nums, target):
    seen = {}  # Hash map: value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:  # O(1) lookup
            return [seen[complement], i]
        seen[num] = i  # O(1) insert
    return []
```

---

### Hash Implementation
**Data Structures & Algorithms for Beginners**

Understanding how hash functions work, collision handling strategies, and the internal mechanics of hash tables provides deeper insight into their performance characteristics.

**How Hash Tables Work:**
1. **Hash Function**: Converts key to an integer (hash code)
2. **Index Calculation**: `index = hash(key) % array_size`
3. **Collision Handling**: When two keys map to same index

**Collision Resolution Strategies:**

**1. Chaining (Separate Chaining)**
- Each bucket contains a linked list of key-value pairs
- When collision occurs, add to the list
- Example: `[bucket0: [(k1,v1), (k2,v2)], bucket1: [(k3,v3)], ...]`

**2. Open Addressing (Linear Probing)**
- When collision occurs, find next available slot
- Probe sequence: `(hash(key) + i) % size` where i = 0, 1, 2, ...

**Example:**
```python
# Simplified hash function concept
def simple_hash(key, size):
    return hash(key) % size

# Collision example
keys = ['apple', 'banana', 'cherry']
# If hash('apple') % 10 == 5
# and hash('banana') % 10 == 5 (collision!)
# Chaining: bucket[5] = [('apple', val1), ('banana', val2)]
# Linear Probing: bucket[5] = ('apple', val1), bucket[6] = ('banana', val2)
```

**Key Insights:**
- Good hash function distributes keys evenly
- Load factor (elements/buckets) affects performance
- Rehashing occurs when load factor gets too high

---

### Prefix Sums
**Advanced Algorithms**

Prefix sums allow efficient range sum queries and are useful for problems involving cumulative operations, subarray sums, and related computations.

**What are Prefix Sums?**
A prefix sum array stores the cumulative sum of elements up to each index. This allows O(1) range sum queries instead of O(n) recalculation.

**Basic Concept:**
For array `nums = [1, 2, 3, 4, 5]`:
- **Prefix sum array**: `prefix = [1, 3, 6, 10, 15]`
  - `prefix[0] = nums[0] = 1`
  - `prefix[1] = nums[0] + nums[1] = 1 + 2 = 3`
  - `prefix[2] = nums[0] + nums[1] + nums[2] = 1 + 2 + 3 = 6`
  - And so on...

**Range Sum Query:**
To get sum from index `i` to `j`:
- **Without prefix sum**: O(n) - iterate and sum
- **With prefix sum**: O(1) - `prefix[j] - prefix[i-1]`

**Example:**
```python
def prefix_sum_example(nums):
    n = len(nums)
    prefix = [0] * n
    prefix[0] = nums[0]
    
    # Build prefix sum array
    for i in range(1, n):
        prefix[i] = prefix[i-1] + nums[i]
    
    # Query: sum from index 2 to 4
    # nums[2:5] = [3, 4, 5], sum = 12
    # Using prefix: prefix[4] - prefix[1] = 15 - 3 = 12
    return prefix

nums = [1, 2, 3, 4, 5]
prefix = prefix_sum_example(nums)
# prefix = [1, 3, 6, 10, 15]
```

**Prefix Multiplication (Product of Array Except Self):**

The same concept applies to products! Instead of cumulative sums, we use cumulative products.

**Problem 1.7: Product of Array Except Self**
Given `nums = [1, 2, 4, 6]`, find product of all elements except `nums[i]` for each `i`.

**Solution using Prefix and Suffix Products:**

**Step 1: Prefix Products (Left Side)**
Calculate product of all elements **before** each index:
```python
nums = [1, 2, 4, 6]
prefix = [1, 1, 2, 8]

# Explanation:
# prefix[0] = 1        (no elements before index 0)
# prefix[1] = 1        (product of elements before index 1: nums[0] = 1)
# prefix[2] = 2        (product of elements before index 2: nums[0] * nums[1] = 1 * 2 = 2)
# prefix[3] = 8        (product of elements before index 3: nums[0] * nums[1] * nums[2] = 1 * 2 * 4 = 8)
```

**Step 2: Suffix Products (Right Side)**
Calculate product of all elements **after** each index:
```python
nums = [1, 2, 4, 6]
suffix = [48, 24, 6, 1]

# Explanation (calculated from right to left):
# suffix[3] = 1        (no elements after index 3)
# suffix[2] = 6        (product of elements after index 2: nums[3] = 6)
# suffix[1] = 24       (product of elements after index 1: nums[2] * nums[3] = 4 * 6 = 24)
# suffix[0] = 48       (product of elements after index 0: nums[1] * nums[2] * nums[3] = 2 * 4 * 6 = 48)
```

**Step 3: Combine Prefix and Suffix**
For each index `i`, multiply prefix[i] (left side) with suffix[i] (right side):
```python
result[0] = prefix[0] * suffix[0] = 1 * 48 = 48   # Product except nums[0]: 2*4*6 = 48 ✓
result[1] = prefix[1] * suffix[1] = 1 * 24 = 24   # Product except nums[1]: 1*4*6 = 24 ✓
result[2] = prefix[2] * suffix[2] = 2 * 6  = 12   # Product except nums[2]: 1*2*6 = 12 ✓
result[3] = prefix[3] * suffix[3] = 8 * 1  = 8    # Product except nums[3]: 1*2*4 = 8  ✓
```

**Visual Representation:**
```
nums =    [1,   2,   4,   6]
          ↓    ↓    ↓    ↓
prefix =  [1,   1,   2,   8]  ← Products of elements to the LEFT
suffix =  [48,  24,  6,   1]  ← Products of elements to the RIGHT
          ↓    ↓    ↓    ↓
result =  [48,  24,  12,  8]  ← prefix[i] * suffix[i]
```

**Why This Works:**
- For index `i`, we need: `nums[0] * nums[1] * ... * nums[i-1] * nums[i+1] * ... * nums[n-1]`
- `prefix[i]` gives us: `nums[0] * nums[1] * ... * nums[i-1]` (left side)
- `suffix[i]` gives us: `nums[i+1] * nums[i+2] * ... * nums[n-1]` (right side)
- Multiplying them gives us exactly what we need!

**Time Complexity:** O(n) - two passes through the array
**Space Complexity:** O(n) - for prefix and suffix arrays (can be optimized to O(1) using output array)

**Common Applications:**
- Range sum queries
- Subarray sum problems
- Cumulative operations
- Product calculations (as in this problem)

## Resources

- [Array Data Structure - GeeksforGeeks](https://www.geeksforgeeks.org/dsa/array-data-structure/)
- [Hashing in Data Structure - GeeksforGeeks](https://www.geeksforgeeks.org/dsa/hashing-data-structure/)
- [Introduction to Hashing - GeeksforGeeks](https://www.geeksforgeeks.org/dsa/introduction-to-hashing-2/)
- [Applications of Hashing - GeeksforGeeks](https://www.geeksforgeeks.org/dsa/applications-of-hashing/)
- [DSA Tutorial - GeeksforGeeks](https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/)