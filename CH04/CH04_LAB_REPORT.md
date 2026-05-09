# Lab 04: Quicksort

## Student Information
- **Name:** [Annabel Shaw]
- **Date:** [2/21/2026]

## Quicksort Concepts

### Divide and Conquer
[ Splitting one group of items into smaller and smaller groups, then adding them together in order]

### The Three Steps
1. **Choose pivot:** [The comparison item]
2. **Partition:** [Splitting based on the pivot]
3. **Recurse and combine:** [Continue pivot and pattern until strings are individual arrays, then combineing them all in order]

## Tracing Quicksort

### Trace: quicksort([3, 5, 2, 1, 4])
[P1=3
2,1   54
p2=2    p3=5
1   2   3  4  5
1,2,3,4,5]

## Complexity Analysis

| Case | Time Complexity | Why? |
|------|----------------|------|
| Best | O(n log n) | [best case is same as average] |
| Average | O(n log n) | [looks at about every other element each time its split] |
| Worst | O(n²) | [if its already sorted the code will go through each element twice] |

## Reflection Questions

1. What happens if the array is already sorted and you always pick the first element as pivot?
   It will be the worst case on time to run, having to search through each individual element.

2. How could you improve pivot selection to avoid worst-case performance?
    Random element or median element, so it does not pull the first element and has a better chance of being the best outcome.

3. How does quicksort compare to other sorting algorithms you know (e.g., bubble sort, merge sort)?
   Quicksort is more consistently the best case scenario than other well known algorithms.

4. Why do we use `array[1:]` instead of `array` when building the less and greater lists?
    Array[1:] makes the reversion end, by counting down as it calls. array will result in an endless loop.

