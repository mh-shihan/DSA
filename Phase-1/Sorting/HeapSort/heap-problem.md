# K Largest Elements in an Array

## Problem Statement

Find the **k largest elements** from an array of integers.

## Constraints

- Array can contain both positive and negative integers
- k ≤ array length
- Elements can be duplicates

## Examples

### Example 1

```
Input:  arr = [3, 2, 1, 5, 6, 4], k = 2
Output: [5, 6]
```

### Example 2

```
Input:  arr = [1, 2, 3, 4, 5], k = 3
Output: [3, 4, 5]
```

### Example 3

```
Input:  arr = [10], k = 1
Output: [10]
```

## Approaches

### 1. **Min Heap (Optimal - O(n log k))**

**Time Complexity:** O(n log k)  
**Space Complexity:** O(k)

- Maintain a min-heap of size k
- For each element, if heap size < k, add it
- If element > min element in heap, remove min and insert new element
- Final heap contains k largest elements

**Best when:** k is much smaller than n

### 2. **Sorting (Simple - O(n log n))**

**Time Complexity:** O(n log n)  
**Space Complexity:** O(1) or O(n)

- Sort array in descending order
- Return first k elements
- Simple but not optimal for large arrays with small k

### 3. **Max Heap (O(n + k log n))**

**Time Complexity:** O(n + k log n)  
**Space Complexity:** O(n)

- Create max heap from entire array
- Extract k largest elements one by one
- Good when k is significant portion of n

## Key Concepts

- **Heap:** Complete binary tree with heap property
- **Min Heap:** Parent ≤ Children (smallest at root)
- **Max Heap:** Parent ≥ Children (largest at root)
- **Priority Queue:** Efficient for min/max operations

## Related Topics

- Heap operations (push, pop, heapify)
- Priority Queue implementation
- Top K elements variants
- Kth largest element
