"""
https://leetcode.com/problems/reverse-linked-list-ii/submissions/1213534074

Problem Statement
    Given the head of a singly linked list and two integers left and right where left <= right,
    reverse the nodes of the list from position left to position right, and return the reversed list.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode|None, left: int, right: int) ->ListNode|None:
        i=1
        curr_node = head
        prev_node = None
        while curr_node and i<left:
            prev_node = curr_node
            curr_node = curr_node.next
            i+=1
        #current node is at left
        last_node_of_first_part = prev_node
        last_node_of_second_part = curr_node

        prev_node = None
        while curr_node and i<=right:
            next_node = curr_node.next
            curr_node.next = prev_node

            prev_node = curr_node
            curr_node = next_node
            i+=1

        if last_node_of_first_part:
            #prev_node is now the first node of the second part
            last_node_of_first_part.next = prev_node
        else:
            #case where linkedlist left==1 (in this case reversed head should be updated as head)
            #this means left==1 so we are changing the first node(head) of the LL
            head = prev_node
        last_node_of_second_part.next = curr_node
        return head
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class SolutionWithDummyNodeToAvoidEdgeCases:
    def reverseBetween(self, head:ListNode|None, left: int, right: int) -> ListNode|None:
        i=1
        #introduce dummy node to avoid edge cases
        dummy_head = ListNode(None,head)
        curr_node = dummy_head
        prev_node = None
        while curr_node and i<=left:
            prev_node = curr_node
            curr_node = curr_node.next
            i+=1
        #current node is at left
        last_node_of_first_part = prev_node
        last_node_of_second_part = curr_node

        prev_node = None
        while curr_node and i<=right+1:
            next_node = curr_node.next
            curr_node.next = prev_node

            prev_node = curr_node
            curr_node = next_node
            i+=1

        last_node_of_first_part.next = prev_node
        last_node_of_second_part.next = curr_node
        return dummy_head.next
        