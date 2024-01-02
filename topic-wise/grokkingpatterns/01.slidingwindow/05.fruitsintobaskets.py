"""
Fruits into Baskets

Problem Statement

    Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
    You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
    Write a function to return the maximum number of fruits in both the baskets.

Example 1:

    Input: Fruit=['A', 'B', 'C', 'A', 'C']
    Output: 3
    Explanation: We can put 2 'C' in one basket and one 'A' in 
    the other from the subarray ['C', 'A', 'C']
    
Example 2:

    Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
    Output: 5
    Explanation: We can put 3 'B' in one basket and two 'C' in 
    the other basket. 
    This can be done if we start with the second letter: 
    ['B', 'C', 'B', 'B', 'C']

Solution

    This problem follows the Sliding Window pattern and is quite similar to Longest Substring with K Distinct Characters. 
    In this problem, we need to find the length of the longest subarray with no more than two distinct characters (or fruit types!). 
    
    This transforms the current problem into Longest Substring with K Distinct Characters where K=2.
"""

def fruits_into_baskets(array:list[int])->int:
    window_end = 0
    window_start = 0
    hashmap :dict[str,int] = {}
    for i in range(len(array)):
        window_end+=1
        hashmap[array[i]] = hashmap.get(array[i],0)+1
        while len(hashmap)>2:
            hashmap[array[window_start]]-=1
            if hashmap[array[window_start]]==0:
                hashmap.pop(array[window_start])
            window_start+=1
    print(f"Fruits in basket are {array[window_start:window_end+1]}")
    return window_end-window_start

if __name__=="__main__":
    print(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))
    print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))
