# Chapter 1: [Introduction to Algorithms] — Lab Report

## Student Information
- **Name:** [Annabel Shaw]
- **Date:** [5/6/26]
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** [Compares linear search time to binary search time in Big O measurements.
- Big O compares the amount of calls instead of seconds to properly measure algorithms negating computer specs]
- **Time complexity:** [linear search is O(n) however binary search is O(log n)]
- **When to use it:** [Linear search is better for shorter lists. Binary search is better in longer listest.]

## Test Results
[Paste your program output, measurement table, or sample run.
 Use a Markdown table where appropriate.]

| Input                                 | Result                                           | Notes |
|----------------                       |--------                                          |-------|
|     a sorted list of 128 names        |   Searching for: 75                              |       |
|                                       |   Linear search time: 0.00000405 seconds         |       |
|                                       |    Binary search time: 0.00000286 seconds        |       |
|                                       |    Linear search result: 74                      |       |
|                                       |    Binary search result: 74                      |       |
|                                       |    Binary search is 1.42x faster                 |       |
|                                       |                                                  |       |
|                                       |   Searching for: 10                              |       |
|                                       |    Linear search time: 0.00000167 seconds        |       |
|                                       |    Binary search time: 0.00000167 seconds        |       |
|                                       |    Linear search result: 9                       |       |
|                                       |    Binary search result: 9                       |       |
|                                       |    Binary search is 1.00x faster                 |       |
|                                       |                                                  |       |
|                                       |    Searching for: 90                             |       |
|                                       |    Linear search time: 0.00000286 seconds        |       |
|                                       |    Binary search time: 0.00000167 seconds        |       |
|                                       |    Linear search result: 89                      |       |
|                                       |    Binary search result: 89                      |       |
|                                       |   Binary search is 1.71x faster                  |       |
|                                       |                                                  |       |
|                                       |    Searching for: 200                            |       |
|                                       |    Linear search time: 0.00000381 seconds        |       |
|                                       |    Binary search time: 0.00000191 seconds        |       |
|                                       |    Linear search result: None                    |       |
|                                       |    Binary search result: None                    |       |
|                                       |    Binary search is 2.00x faster                 |       |
|                                       |                                                  |       |
|                                       |    Lab Challenge Answer:                         |       |
|                                       |    Maximum steps for binary search in 128 items: |       |
|                                       |    log2(128) = 7 steps maximum                   |       |

## Reflection Questions

1. **[What is the amount of operations Binary search would make searching through the whole list]**
   [Binary has a max of 7 operations to this 128 item list.]

2. **[What is the amount of operations Liner search would make searching through the whole list]**
   [Liner search has a max of 128 on this 128 item list to transvers.]

3. **[Why are the time complexities so different?]**
   [Your answer in 2-3 sentences.]

## Challenges Encountered
[Not having access or the ability to learn through the first lab was probably the biggest challenge of this lab. I wish I had access to it to have the ability to learn how it runs earlyer.]
