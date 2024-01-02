"""
Problem Statement: Circular Loop Array

    You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:

        If nums[i] is positive, move nums[i] steps forward, and
        If nums[i] is negative, move nums[i] steps backward.

    Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.

    A cycle in the array consists of a sequence of indices seq of length k where:

        Following the movement rules above results in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
        Every nums[seq[j]] is either all positive or all negative.
        k > 1
        Return true if there is a cycle in nums, or false otherwise.

Example 1:

    Input: nums = [2,-1,1,2,2]
    Output: true
    Explanation: The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
    We can see the cycle 0 --> 2 --> 3 --> 0 --> ..., and all of its nodes are white (jumping in the same direction).

Example 2:

    Input: nums = [-1,-2,-3,-4,-5,6]
    Output: false
    Explanation: The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
    The only cycle is of size 1, so we return false.

Example 3:

    Input: nums = [1,-1,5,1,4]
    Output: true
    Explanation: The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
    We can see the cycle 0 --> 1 --> 0 --> ..., and while it is of size > 1, it has a node jumping forward and a node jumping backward, so it is not a cycle.
    We can see the cycle 3 --> 4 --> 3 --> ..., and all of its nodes are white (jumping in the same direction).
    

Constraints:

    1 <= nums.length <= 5000
    -1000 <= nums[i] <= 1000
    nums[i] != 0
 

Follow up: 
    Could you solve it in O(n) time complexity and O(1) extra space complexity?
"""

def circular_array_loop(nums: list[int]) -> bool:
        n = len(nums)
        def get_next_idx(current_idx:int,is_forward:bool)->int:
            is_current_direction_forward = nums[current_idx]>=0
            if is_current_direction_forward!=is_forward:
                #As Every nums[seq[j]] is either all positive or all negative
                return -1
            idx = current_idx+nums[current_idx]
            while idx<0:
                if idx+n<=n-1: idx+=n
            if idx>n-1:
                idx = idx%n
            if idx==current_idx:
                #it is a cycle so break while loop
                return -1
            return idx
        
        for i in range(n):
            slow_ptr=fast_ptr=i
            while True:
                slow_ptr = get_next_idx(slow_ptr,is_forward=nums[i]>=0)        
                fast_ptr = get_next_idx(fast_ptr,is_forward=nums[i]>=0)
                if fast_ptr!=-1:
                    #another step for fast ptr
                    fast_ptr = get_next_idx(fast_ptr,is_forward=nums[i]>=0)
                if slow_ptr==-1 or fast_ptr==-1 or slow_ptr==fast_ptr:
                    break

            if slow_ptr!=-1 and slow_ptr==fast_ptr:
                return True
        return False

if __name__=="__main__":
    print(circular_array_loop([2,-1,1,2,2]))
    print(circular_array_loop([1,-1,5,1,4]))
    print(circular_array_loop([-1,-2,-3,-4,-5,6]))