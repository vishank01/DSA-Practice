"""
https://leetcode.com/problems/linked-list-cycle/submissions/1132135773
https://leetcode.com/problems/linked-list-cycle-ii/submissions/1132154206

Problem Statement:

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Constraints:

    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self,):
        return f"Linked List Node with Value {self.val}"

def has_cycle(head: ListNode) -> bool:
    """
    Approach:
        Imagine we have a slow and a fast pointer to traverse the LinkedList. In each iteration, the slow pointer moves one step and the fast pointer moves two steps. This gives us two conclusions:

        If the LinkedList doesn’t have a cycle in it, the fast pointer will reach the end of the LinkedList before the slow pointer to reveal that there is no cycle in the LinkedList.
        The slow pointer will never be able to catch up to the fast pointer if there is no cycle in the LinkedList.
        If the LinkedList has a cycle, the fast pointer enters the cycle first, followed by the slow pointer. After this, both pointers will keep moving in the cycle infinitely. If at any stage both of these pointers meet, we can conclude that the LinkedList has a cycle in it. Let’s analyze if it is possible for the two pointers to meet. When the fast pointer is approaching the slow pointer from behind we have two possibilities:

            1. The fast pointer is one step behind the slow pointer.
            2. The fast pointer is two steps behind the slow pointer.
        
        All other distances between the fast and slow pointers will reduce to one of these two possibilities. Let’s analyze these scenarios, considering the fast pointer always moves first:

            1. If the fast pointer is one step behind the slow pointer: The fast pointer moves two steps and the slow pointer moves one step, and they both meet.
            2. If the fast pointer is two steps behind the slow pointer: The fast pointer moves two steps and the slow pointer moves one step. After the moves, the fast pointer will be one step behind the slow pointer, which reduces this scenario to the first scenario. This means that the two pointers will meet in the next iteration.
        
        This concludes that the two pointers will definitely meet if the LinkedList has a cycle.
    """
    fast_ptr = slow_ptr = head
    while fast_ptr!=None and fast_ptr.next!=None:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
        if fast_ptr==slow_ptr:
            return True
    return False
    
def find_cycle_length(head:ListNode)->int:
    fast_ptr = slow_ptr = head

    def find_cycle_length(slow_ptr:ListNode)->int:
        cnt = 0
        tmp_ptr = slow_ptr
        while True:
            tmp_ptr = tmp_ptr.next
            cnt+=1
            if tmp_ptr==slow_ptr:
                break
        return cnt

    while fast_ptr!=None and fast_ptr.next!=None:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
        if fast_ptr==slow_ptr:
            #cycle is detected
            return find_cycle_length(slow_ptr)
        
    return 0

def find_start_of_linked_list_cycle(head:ListNode)->ListNode:
    """
        If we know the length of the LinkedList cycle, we can find the start of the cycle through the following steps:
            1. Take two pointers. Let’s call them pointer1 and pointer2.
            2. Initialize both pointers to point to the start of the LinkedList.
            3. We can find the length of the LinkedList cycle using the approach discussed in LinkedList Cycle. Let’s assume that the length of the cycle is K nodes.
            4. Move pointer 2 ahead by K nodes.
            5. Now, keep incrementing pointer1 and pointer2 until they both meet.
            6. As pointer 2 is K nodes ahead of pointer1, which means, pointer2 must have completed one loop in the cycle when both pointers meet. Their meeting point will be the start of the cycle.
    """
    fast_ptr = slow_ptr = head

    def find_start_of_cycle(head:ListNode,length:int)->ListNode:
        ptr1 = ptr2 = head
        while length>0:
            ptr2 = ptr2.next
            length-=1
        #now ptr2 is ahead of ptr1 by k nodes (where k is length of loop)
        #now move both pointers with same speed, once they meet it is the starting point as ptr2 is ahead of 
        #ptr1 by k nodes, ptr2 completes cycle and meets ptr1
        while ptr1!=ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1

    length = 0
    while fast_ptr!=None and fast_ptr.next!=None:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
        if fast_ptr == slow_ptr:
            #cycle is detected
            length = find_cycle_length(slow_ptr)
            break
    return find_start_of_cycle(head,length)

    
if __name__=="__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = head.next.next
    head.next.next.next.next.next.next = head.next.next.next
    head.next.next.next.next.next.next = head
    print(has_cycle(head))
    print(find_cycle_length(head))
    print(find_start_of_linked_list_cycle(head))