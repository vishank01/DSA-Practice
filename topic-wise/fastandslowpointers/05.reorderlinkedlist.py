"""
https://leetcode.com/problems/reorder-list/submissions/1132444621

Problem Statement:
    Given the head of a Singly LinkedList, write a method to modify the LinkedList such that 
    the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order. 
    So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.
    
    Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

Example 1:

    Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
    Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null 

Example 2:

    Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
    Output: 2 -> 10 -> 4 -> 8 -> 6 -> null
    This problem shares similarities with Palindrome LinkedList. To rearrange the given LinkedList we will follow the following steps:

Approach:
    1. We can use the Fast & Slow pointers method similar to Middle of the LinkedList to find the middle node of the LinkedList.
    2. Once we have the middle of the LinkedList, we will reverse the second half of the LinkedList.
    3. Finally, we’ll iterate through the first half and the reversed second half to produce a LinkedList in the required order.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_list(self):
        result = ""
        tmp = self
        while tmp!=None:
            result+=f"{tmp.val} "
            tmp = tmp.next
        print(result)

    def __repr__(self,):
        return f"Linked List Node with Value {self.val}"
    
def reorder_list(head:ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    fast_ptr=slow_ptr=head
    while fast_ptr!=None and fast_ptr.next!=None:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next

    head_second_half=reverse(slow_ptr)
    head_first_half = head

    #loop first half until slow_ptr and second half from slow_ptr to End
    while head_first_half!=slow_ptr and head_second_half!=None:
        first_half_next_node = head_first_half.next
        head_first_half.next = head_second_half
        head_first_half = first_half_next_node

        second_half_next_node = head_second_half.next
        head_second_half.next = head_first_half
        head_second_half = second_half_next_node

    #second half has broken while loop so head first half should be updatd with None
    if head_first_half!=None:
        head_first_half.next = None
        
    return head

def reverse(head:ListNode)->ListNode:
    prev = None
    while head!=None:
        next_node = head.next
        head.next = prev
        
        prev = head
        head = next_node
    return prev

if __name__=="__main__":
    head = ListNode(2)
    head.next = ListNode(4)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(8)
    head.next.next.next.next = ListNode(10)
    head.next.next.next.next.next = ListNode(12)

    reorder_list(head)
    head.print_list()#2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null 
