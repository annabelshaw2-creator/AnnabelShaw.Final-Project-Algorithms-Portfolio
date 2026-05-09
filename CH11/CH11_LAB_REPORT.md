# Chapter 11: [Dynamic Programming] — Lab Report

## Student Information
- **Name:** [Annabel Shaw]
- **Date:** [5/9/26]
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** [Takes the greedy algorithm of chapter 10 and separates it into several smaller problems to compound at the end]
- **Time complexity:** [0(SC)]
- **When to use it:** [Dynamic programing can be used in any algorithm to help simply it down]

## Test Results
[Paste your program output, measurement table, or sample run.
 Use a Markdown table where appropriate.]

| Input          | Result | Notes |
|----------------|--------|-------|
|       items = [||capacity = 6         ||
  |  ("GUITAR", 1, 1500),|                           1           2           3           4           5           6||
  |  ("STEREO", 4, 3000),|GUITAR          $1500(G)    $1500(G)    $1500(G)    $1500(G)    $1500(G)    $1500(G)||
  |  ("LAPTOP", 3, 2000),|STEREO          $1500(G)    $1500(G)    $1500(G)    $3000(S)   $4500(GS)   $4500(GS)||
  |  ("iPHONE", 1, 2000),|LAPTOP          $1500(G)    $1500(G)    $2000(L)   $3500(GL)   $4500(GS)   $4500(GS)||
  |  ("BOOK", 2, 100),|iPHONE          $2000(i)   $3500(Gi)   $3500(Gi)   $4000(Li)  $5500(GLi)  $6500(GSi)||
 |   ("GOLD BAR", 1, 30000),|BOOK            $2000(i)   $3500(Gi)   $3500(Gi)   $4000(Li)  $5500(GLi)  $6500(GSi)||
|]| GOLD BAR       $30000(G)  $32000(iG) $33500(GiG) $33500(GiG) $34000(LiG)$35500(GLiG)    |  |



## Reflection Questions

1. **[What is Dynamic programing]**
   [Dynamic programming is simplifying a big problem into several smaller problems to make the program easier to solve.]

2. **[What is Greedy algorithm]**
   [A greedy algorithm is a simple algorithm of picking the better options without checking each possibility of outcome.]


## Challenges Encountered
[The only problem I had was my graph was only printing the guitar line, the spacing was slightly off and it wasn't reading the print mod correctly; it was easy to fix once found.]

