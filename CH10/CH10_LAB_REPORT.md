# Chapter 10: [Truck] — Lab Report
## Student Information
Name: [Annabel shaw]
Date: [4/19/26]

## Algorithm Analysis: Greedy Truck Packing Algorithm

### Algorithm Understanding
1) What type of problem is this algorithm solving?
[packing problem]

2) Is this greedy algorithm guaranteed to produce the optimal solution? Why or why not?
[No, it does not consider dimensions or what space would be optimally filled later.]

3) What is the greedy choice made in this algorithm?
[To not calculate every possible load, just the one that works enough.]

## Implementation Questions
1) Why do we sort the boxes in descending order of volume before packing?
[To get the biggest possible first(greedy algorithm).]

2) What would happen if we sorted the boxes in ascending order instead?
[A larger amount of value can be left unpacked in the truck.]

3) Why do we keep track of used_volume?
[To calculate if you can put the next box in the truck.]

## Extension: Dimension Constraints
1) Why is checking only volume not sufficient for real-world packing?
[Dimensions of the box is usually different the a round volume number.]

2) Give an example where a box fits by volume but not by dimensions.
[perfect cubes]

3) How would you modify the algorithm to check dimension constraints before packing a box?
[Have a counter for width, height, and length instead of just volume.]

## Reflection Questions
1) What is a limitation of this greedy approach? Provide a scenario where it fails to find the optimal solution.
[If packed optimally there might be space for another box.]

2) How is this problem related to the Knapsack Problem?
[Knapsack takes the biggest value that still fits in the sack, which is practically the same as the cargo truck sulution.]

3) What type of algorithm would guarantee an optimal solution for this problem? What is the tradeoff?
[Graphing algorithm; calculation time.]

4) If the truck had weight limits in addition to volume, how would the algorithm need to change?
[it would have to calculate weight and volume.]

5) Why are greedy algorithms often preferred despite not always being optimal?
[The tradeoff is not worth it for it can find the next best thing or the most optimal already.]

