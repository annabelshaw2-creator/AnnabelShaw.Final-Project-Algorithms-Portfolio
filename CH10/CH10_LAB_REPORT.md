Student Information
Name: [Annabel shaw]
Date: [4/19/26]
Algorithm Analysis: Greedy Truck Packing Algorithm

Algorithm Understanding
What type of problem is this algorithm solving?
[packing problem]

Is this greedy algorithm guaranteed to produce the optimal solution? Why or why not?
[no, it dose not consder demetions or what space would be optmalily filled later]

What is the greedy choice made in this algorithm?
[to not calculate every possable load just the one that works enough]

Implementation Questions
Why do we sort the boxes in descending order of volume before packing?
[to get the bigest possable first(greedy algorithm)]

What would happen if we sorted the boxes in ascending order instead?
[A larger amount of value can be left unpacked in the truck]

Why do we keep track of used_volume?
[to calculate if you can put the next box in the truck]

Extension: Dimension Constraints
Why is checking only volume not sufficient for real-world packing?
[demations of the box is ussaly different the a round valume number]

Give an example where a box fits by volume but not by dimensions.
[perfict cubes]

How would you modify the algorithm to check dimension constraints before packing a box?
[have a counter for width, height, and length insded of just volume]

Reflection Questions
What is a limitation of this greedy approach? Provide a scenario where it fails to find the optimal solution.
[if packed optamilly there might be space for another box.]

How is this problem related to the Knapsack Problem?
[knapsack takes the bigest value that still fits in the sack, wich is practicly the same as the cargo truk sulution.]

What type of algorithm would guarantee an optimal solution for this problem? What is the tradeoff?
[graphing algorithm; caluclation time.]

If the truck had weight limits in addition to volume, how would the algorithm need to change?
[it would have to caluclate weight and volume.]

Why are greedy algorithms often preferred despite not always being optimal?
[The tradeoff is not worth it for it can find the next best thing or the most optamilly alredy.]
