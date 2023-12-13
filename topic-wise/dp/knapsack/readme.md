# Knapsack 0/1

Given N items where each item has some weight and profit associated with it and also given a bag with capacity W, [i.e., the bag can hold at most W weight in it]. The task is to put the items into the bag such that the sum of profits associated with them is the maximum possible.

**_(Note: The constraint here is we can either put an item completely into the bag or cannot put it at all [It is not possible to put a part of an item into the bag]._\***

_**Input**_: N = 3, W = 4, profit[] = {1, 2, 3}, weight[] = {4, 5, 1}
_**Output**_: 3
_**Explanation**_: There are two items which have weight less than or equal to 4. If we select the item with weight 4, the possible profit is 1. And if we select the item with weight 1, the possible profit is 3. So the maximum possible profit is 3. Note that we cannot put both the items with weight 4 and 1 together as the capacity of the bag is 4.\_

## Recursion Approach for 0/1 Knapsack Problem

## Naive Approach (Brute-Force)

A simple solution is to consider all subsets of items and calculate the total weight and profit of all subsets. Consider the only subsets whose total weight is smaller than W. From all such subsets, pick the subset with maximum profit.

### Optimal Substructure

The maximum value obtained from ‘N’ items is the max of the following two values.

    Case 1 (include the Nth item): Value of the Nth item plus maximum value obtained by remaining N-1 items and remaining weight i.e. (W-weight of the Nth item).
    Case 2 (exclude the Nth item): Maximum value obtained by N-1 items and W weight.

If the weight of the ‘Nth‘ item is greater than ‘W’, then the Nth item cannot be included

Time Complexity: O(2N)\
Auxiliary Space: O(N),Stack space required for recursion

## Dynamic Programming Approach for 0/1 Knapsack Problem

### Memoization Approach for 0/1 Knapsack Problem

Time Complexity : O(N \* W). As redundant calculations of states are avoided.\
Auxiliary Space : O(N \* W) + O(N). The use of a 2D array data structure for storing intermediate states and O(N) auxiliary stack space(ASS) has been used for recursion stack

## Bottom-up Approach for 0/1 Knapsack Problem

To solve the problem follow the below idea

Since subproblems are evaluated again, this problem has Overlapping Sub-problems property.

Like other typical Dynamic Programming(DP) problems, re-computation of the same subproblems can be avoided by constructing a temporary array K[][] in a bottom-up manner.
