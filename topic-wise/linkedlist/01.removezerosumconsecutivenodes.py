"""
Problem Statement:
    Remove Zero Sum Consecutive Nodes from Linked List
        Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
        After doing so, return the head of the final linked list.You may return any such answer. 
        (Note that in the examples below, all sequences are serializations of ListNode objects.)
Example 1:
    Input: head = [1,2,-3,3,1]
    Output: [3,1]
    Note: The answer [1,2,1] would also be accepted.

Example 2:
    Input: head = [1,2,3,-3,4]
    Output: [1,2,4]

Example 3:
    Input: head = [1,2,3,-3,-2]
    Output: [1]
    
Constraints:
    The given linked list will contain between 1 and 1000 nodes.
    Each node in the linked list has -1000 <= node.val <= 1000.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    """
        Approach:
            PrefixSum + HashMap
            https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/solutions/4862085/easy-explanation-prefixsum-hashmap-c-java-python3
        Intuition:
            1. To approach this problem, we can utilize a hashmap to keep track of the cumulative sum encountered while traversing the linked list. 
            2. If we encounter the same cumulative sum again, it means the subsequence between the current node and the node with the same cumulative sum sums to zero, 
            3. so we can remove that subsequence. To facilitate this removal, we maintain a dummy node to handle cases where the entire linked list needs to be modified.
    """
    def removeZeroSumSublists(self, head:ListNode|None) -> ListNode|None:
        mp = {}
        prefix_sum = 0
        #Initialize a dummy node to handle cases where the entire linked list needs to be modified.
        dummy = ListNode(0,head)
        ptr = dummy
        while ptr:
            prefix_sum+=ptr.val
            if prefix_sum in mp:
                start = mp[prefix_sum]
                tmp = start
                psum = prefix_sum
                #remove all prefix sums that can be formed with removed window elements
                while tmp!=ptr:
                    tmp = tmp.next
                    psum+=tmp.val
                    if tmp!=ptr:
                        mp.pop(psum,None)
                start.next = ptr.next
            else:
                mp[prefix_sum] = ptr
            ptr = ptr.next
        return dummy.next

