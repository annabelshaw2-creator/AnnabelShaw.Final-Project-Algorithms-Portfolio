# Lab 2: Selection Sort

## Student Information
- **Name:** [Annabel Shaw]
- **Date:** [2/6/26]

## Algorithm Summary
sort.py is the modes used in main.py for different outputs from the values in cities.json. main.py uses sort.py to find the smallest cities by
population, largest cities by population, then using this to calculate array vs linked list in processing memory and time, also then comparing
the made program to the built in python program.
### Selection Sort
- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **How it works:** [goes through the entire array searching for the current smallest value until all items are sorted in order.]

## Array vs Linked List Analysis

| Operation | Array | Linked List | Why? |
|-----------|-------|-------------|------|
| Read      | O(1)  | O(n)        |   you have to start from the beginning of a list with an array you can quickly go to any point    |
| Insert    | O(n)  | O(1)        |  Arrays size can nor be changed and lists can be added to easily    |
| Delete    | O(n)  | O(1)        |    it is more complicated to remove a value from and array then a list  |

## Test Results
[Starting sandbox...
Uploading files...
$ python3 main.py

user@e2b:~$ cd /home/user && python3 main.py
Loaded 20 cities

============================================================
PART 1: SELECTION SORT
============================================================

Sorting cities by population (smallest first)...
Selection Sort: 190 comparisons, 10 swaps

Top 5 smallest cities:
  McAllen: 142,210
  Pasadena: 151,950
  Killeen: 153,095
  Brownsville: 183,392
  McKinney: 195,308

Sorting cities by population (largest first)...
Selection Sort: 190 comparisons, 0 swaps

Top 5 largest cities:
  Houston: 2,304,580
  San Antonio: 1,547,253
  Dallas: 1,304,379
  Austin: 978,908
  Fort Worth: 918,915

----------------------------------------
Comparison with Python's built-in sort:
Python Built-in Sort: O(n log n) - Timsort

============================================================
PART 2: ARRAY VS LINKED LIST
============================================================

--- Python List (Array) Operations ---
Array access by index [10]: 'Lubbock' - O(1) - 0.95 µs
Array insert at beginning: O(n) - 0.95 µs

--- Linked List Operations ---
Created linked list with 20 cities
LinkedList insert at head: O(1) - 2.38 µs

Searching for 'Dallas' in linked list...
LinkedList Search: Found in 4 comparisons

============================================================
PART 3: BIG O SUMMARY
============================================================

    Selection Sort: O(n²)
    - For 20 cities: ~190 comparisons
    - For 1000 cities: ~500,000 comparisons
    - For 1,000,000 cities: ~500 billion comparisons!
    
    Python's Timsort: O(n log n)  
    - For 20 cities: ~86 comparisons
    - For 1000 cities: ~10,000 comparisons
    - For 1,000,000 cities: ~20 million comparisons
    
    Array vs Linked List:
    ┌───────────┬─────────┬─────────────┐
    │ Operation │  Array  │ Linked List │
    ├───────────┼─────────┼─────────────┤
    │ Read      │  O(1)   │    O(n)     │
    │ Insert    │  O(n)   │    O(1)*    │
    │ Delete    │  O(n)   │    O(1)*    │
    └───────────┴─────────┴─────────────┘]

## Reflection Questions

1. Why is selection sort O(n²)?
 If the order of the list is in reverse of what is wanted it will take the computer the entire list length for each item of the list to circle through and sort properly.
2. When would you choose a linked list over an array?
    for lists that are constantly getting added too and removed from.
3. Why does Python use arrays (lists) as the default sequence type?

    Quicker access to data points.

