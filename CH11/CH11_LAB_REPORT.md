# Chapter X: [Dynamic Progarming] — Lab Report

## Student Information
- **Name:** [Annabel Shaw]
- **Date:** [5/9/26]
- **Course:** COSC 2436

## Algorithm Summary
- **How it works:** [2-3 sentence plain-English explanation]
- **Time complexity:** [e.g., O(log n), O(n²), O(V + E)]
- **When to use it:** [What problems is this algorithm well-suited for?]

## Test Results
[Paste your program output, measurement table, or sample run.
 Use a Markdown table where appropriate.]

| Input          | Result | Notes |
|----------------|--------|-------|
|       items = [
    ("GUITAR", 1, 1500),
    ("STEREO", 4, 3000),
    ("LAPTOP", 3, 2000),
    ("iPHONE", 1, 2000),
    ("BOOK", 2, 100),
    ("GOLD BAR", 1, 30000),
]

capacity = 6         |                           1           2           3           4           5           6
GUITAR          $1500(G)    $1500(G)    $1500(G)    $1500(G)    $1500(G)    $1500(G)
STEREO          $1500(G)    $1500(G)    $1500(G)    $3000(S)   $4500(GS)   $4500(GS)
LAPTOP          $1500(G)    $1500(G)    $2000(L)   $3500(GL)   $4500(GS)   $4500(GS)
iPHONE          $2000(i)   $3500(Gi)   $3500(Gi)   $4000(Li)  $5500(GLi)  $6500(GSi)
BOOK            $2000(i)   $3500(Gi)   $3500(Gi)   $4000(Li)  $5500(GLi)  $6500(GSi)
GOLD BAR       $30000(G)  $32000(iG) $33500(GiG) $33500(GiG) $34000(LiG)$35500(GLiG)    |       |

## Reflection Questions

1. **[What is]**
   [Your answer in 2-3 sentences.]

2. **[Your second question]**
   [Your answer in 2-3 sentences.]

3. **[Your third question]**
   [Your answer in 2-3 sentences.]

## Challenges Encountered
[Brief paragraph describing what was difficult, what you tried,
 and how you resolved it.]
