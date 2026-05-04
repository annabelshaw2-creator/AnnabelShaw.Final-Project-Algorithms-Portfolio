# Lab 04: Quicksort

## Student Information
- **Name:** [Annabel Shaw]
- **Date:** [2/21/2026]

## Quicksort Concepts

### Divide and Conquer
[spliting one group of items into smaller and smaller groups, then adding them togeter in order]

### The Three Steps
1. **Choose pivot:** [the comparosion item]
2. **Partition:** [spliting based on the pivot]
3. **Recurse and combine:** [contunie pivot and partition utill strings are indiviual arrays then combine them all in order]

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
| Best | O(n log n) | [best case is same as advrage] |
| Average | O(n log n) | [looks at about every other element each time its split] |
| Worst | O(n²) | [if its already sorted the code will go through each element twice] |

## Reflection Questions

1. What happens if the array is already sorted and you always pick the first element as pivot?
    will be worst case on time to run.

2. How could you improve pivot selection to avoid worst-case performance?
    random element or median element.

3. How does quicksort compare to other sorting algorithms you know (e.g., bubble sort, merge sort)?
    more consistanly good.

4. Why do we use `array[1:]` instead of `array` when building the less and greater lists?
    to make the recersion end.
