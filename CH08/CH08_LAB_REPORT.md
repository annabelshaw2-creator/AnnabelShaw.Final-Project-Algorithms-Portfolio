# Chapter 8: [Balanced Trees] — Lab Report


## Student Information
Name: [Annabel Shaw]
Date: [4/5/26]

## Algorithm Analysis
- AVL Trees
- Balance Factor Range: [-1<= x >= 1]
- Why rebalance? [Search time]
- Time Complexity (all operations): O(log n)

## Rotation Cases
|Case|	Imbalance	              |Fix|
|-------|------------|-----------|
|LL	|	[Two floors of left children nodes]    |  [pivot left] |
|RR	|	[Two floors of right children nodes]   |  [pivot right] |
|LR	|	[first flor left, leaf right]          | [pivot right then left] |
|RL	|	[first flor right, leaf left]          | [pivot left then right] |

## Reflection Questions
1) **Why is an unbalanced BST bad?**
    [Increased search and insert]
2) ** How do rotations maintain the BST property?**
    [Maintains two child nodes that are greater than root on left and less on right]
3) **What other self-balancing trees exist?**
    [Splay and black-red]


