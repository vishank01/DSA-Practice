"""
https://leetcode.com/problems/3sum/submissions/1128902352

Problem Statemen: 3Sum

    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets.

Example 1:

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
        nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
        nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
        nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
        The distinct triplets are [-1,0,1] and [-1,-1,2].
        Notice that the order of the output and the order of the triplets does not matter.

Example 2:

    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

Example 3:

    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.
 
Constraints:

    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105
"""

def three_sum(nums:list[int])->set[tuple[int]]:
    """
        Approach:
            nums[i]+nums[start]+nums[end]=0
            nums[start]+nums[end]=-nums[i]
            Now use Two pointer Approach with target value -nums[i]

        Time Complexity:  
            Sorting the array will take O(N * logN). Inner While loop searching for j,k will take O(N). 
            As we are calling it for for every number in the input array, this means that overall func will take O(N * logN + N^2),
            which is asymptotically equivalent to O(N^2).
            
        Space Complexity:
            Ignoring the space required for the output array, the space complexity of the above algorithm will be O(N) which is required for sorting.
    """
    nums.sort()
    n = len(nums)
    output = set()
    for i in range(n-2):
        start,end = i+1,n-1
        while start<end:
            if nums[start]+nums[end]<-nums[i]:
                start+=1
            elif nums[start]+nums[end]>-nums[i]:
                end-=1
            else:
                output.add((nums[i],nums[start],nums[end]))
                start+=1
                end-=1
    return output

if __name__=="__main__":
    print(three_sum([-1,0,1,2,-1,-4]))
    print(three_sum([0,1,1]))