"""
https://leetcode.com/problems/middle-of-the-linked-list/submissions/1132170021

Problem Statement:
    Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.
    If the total number of nodes in the LinkedList is even, return the second middle node.

Approach-1:
    One brute force strategy could be to first count the number of nodes in the LinkedList and then find the middle node in the second iteration. Can we do this in one iteration?

Approach-2:
    We can use the Fast & Slow pointers method such that the fast pointer is always twice the nodes ahead of the slow pointer. 
    This way, when the fast pointer reaches the end of the LinkedList, the slow pointer will be pointing at the middle node.

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self,):
        return f"Linked List Node with Value {self.val}"

def get_middle_ele_of_linked_list(head:ListNode)->ListNode:
    fast_ptr = slow_ptr = head
    while fast_ptr!=None and fast_ptr.next!=None:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
    return slow_ptr

if __name__=="__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    print(get_middle_ele_of_linked_list(head))