# Lab 3: Recursion

## Student Information
- **Name:** [Annabel Shaw]
- **Date:** [2/13/2026]

## Recursion Concepts

### Two Parts of Every Recursive Function
1. **Base Case:** [the ending case]
2. **Recursive Case:** [the looping case]

### The Call Stack
[The call stack is a stack that adds to the top of the pile then calling from the top of the pile before returning the later ellemnts.]

## Function Analysis

| Function | Base Case | Recursive Case | Time Complexity |
|----------|-----------|----------------|-----------------|
| countdown | i <= 0 | countdown(i-1) | O(n) |
| fact | x <= 1 | x * fact(x-1) | O(n) |
| recursive_sum | empty list | first + sum(rest) | O(n) |
| recursive_count | empty list | 1 + count(rest) | O(n) |
| recursive_max | single item | max(first, max(rest)) | O(n) |

## Reflection Questions

1. What happens if you forget the base case?
    Infident loop with stack overflow error.
2. Why is the naive Fibonacci implementation inefficient?
    Fibonacci is an infinite calculation of numbers and will overflow the memory in a recursive loop.
3. Draw the call stack for fact(4).
            (24)
    (24)*1
    (12)*2...
    4*3...


