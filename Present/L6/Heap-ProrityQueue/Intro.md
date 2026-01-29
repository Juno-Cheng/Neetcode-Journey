# Heap-Priority Queue

## Overview

This section covers heap data structures and priority queues, specialized tree-based structures that efficiently support operations requiring access to minimum or maximum elements.

## Topics

### Heap Properties
Data Structures & Algorithms for Beginners

Heaps are complete binary trees that satisfy the heap property: in a min-heap, every parent is smaller than its children, and in a max-heap, every parent is larger. Understanding heap properties, complete binary tree structure, and how heaps maintain their ordering is fundamental for implementing efficient priority-based operations and sorting algorithms.

### Push and Pop
Data Structures & Algorithms for Beginners

Push and pop operations maintain the heap property when inserting new elements or removing the root. Push adds elements at the end and bubbles up to restore the heap property, while pop removes the root, replaces it with the last element, and bubbles down. These operations run in O(log n) time and are essential for all heap-based algorithms.

### Heapify
Data Structures & Algorithms for Beginners

Heapify is the process of converting an array into a valid heap structure by ensuring the heap property holds for all nodes. This operation runs in O(n) time using a bottom-up approach, starting from the last parent node and working upward. Understanding heapify is crucial for building heaps efficiently and implementing heap sort.

### Two Heaps
Advanced Algorithms

Two heaps technique uses both a min-heap and max-heap simultaneously to solve problems requiring tracking both minimum and maximum elements or maintaining medians. This advanced pattern is essential for problems like finding running medians, sliding window problems with dual constraints, and scenarios where you need efficient access to both extremes of a dataset.

## Resources

- [Heap Data Structure - GeeksforGeeks](https://www.geeksforgeeks.org/dsa/heap-data-structure/)
- [Binary Heap - GeeksforGeeks](https://www.geeksforgeeks.org/binary-heap/)
- [Priority Queue - GeeksforGeeks](https://www.geeksforgeeks.org/dsa/priority-queue/)
- [Heap Operations - GeeksforGeeks](https://www.geeksforgeeks.org/dsa/heap-operations/)
- [Heap Sort - GeeksforGeeks](https://www.geeksforgeeks.org/dsa/heap-sort/)
- [DSA Tutorial - GeeksforGeeks](https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/)
