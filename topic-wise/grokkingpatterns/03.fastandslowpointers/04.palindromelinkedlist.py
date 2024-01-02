"""
https://leetcode.com/problems/palindrome-linked-list/submissions/1132195440

Problem Statement:
    Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.
    Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. 
    The algorithm should have O(N) time complexity where N is the number of nodes in the LinkedList.

Example 1:

    Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
    Output: true

Example 2:

    Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
    Output: false

Constraints:

    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self,):
        return f"Linked List Node with Value {self.val}"

def check_if_linked_list_is_palindrome(head:ListNode)->bool:
    fast_ptr = slow_ptr = head
    while fast_ptr!=None and fast_ptr.next!=None:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
    
    reversed_second_half = reverse_linked_list(slow_ptr)
    while head!=slow_ptr and reversed_second_half!=None:
        if head.val !=reversed_second_half.val:
            return False
        head = head.next
        reversed_second_half = reversed_second_half.next

    if head==slow_ptr or reversed_second_half==None:
        return True
    return False


def reverse_linked_list(head:ListNode)->ListNode:
    prev = None
    while head!=None:
        #change direction of next to back wards to head
        next_node = head.next
        #point head to prev which is None
        head.next = prev

        #now update prev as head and head as next
        prev = head
        head = next_node
    return prev


if __name__=="__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    print(check_if_linked_list_is_palindrome(head))