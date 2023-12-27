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

def three_sum(nums:list[int])->list[list[int]]:
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
    output = []
    n = len(nums)
    for i in range(n-2):
        #to avoid duplicates in output
        if i>0 and nums[i]==nums[i-1]:
            continue
        start,end = i+1,n-1
        while start<end:
            if nums[start]+nums[end]<-nums[i]:
                start+=1
            elif nums[start]+nums[end]>-nums[i]:
                end-=1
            else:
                output.append([nums[i],nums[start],nums[end]])
                start+=1
                end-=1
    return output

def three_sum_using_two_sum(nums:list[int])->list[list[int]]:
    """
        we check whether two consecutive elements are equal or not because if they are, we don't want them (solutions need to be unique) 
        and will skip to the next set of numbers. Also, there is an additional constrain in this line that i > 0. 
        This is added to take care of cases like nums = [1,1,1] and target = 3. If we didn't have i > 0, 
        then we'd skip the only correct solution and would return [] as our answer which is wrong (correct answer is [[1,1,1]]
    """
    nums.sort()
    output = []
    n = len(nums)
    for i in range(n-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        search_pairs(nums,i,n,0,output)
    return output

def search_pairs(nums:list[int],first:int,n:int,target:int,output:list[int]):
    i,j = first+1,n-1
    #i and j cannot be equal as numbers should be distinct
    while i<j:
        s = nums[first]+nums[i]+nums[j]
        if s<target:
            i+=1
        elif s>target:
            j-=1
        else:
            output.append([nums[first],nums[i],nums[j]])
            i+=1
            j-=1
            while i<j and nums[i]==nums[i-1]:
                i+=1
            while i<j and nums[j]==nums[j-1]:
                j-=1


if __name__=="__main__":
    print(three_sum_using_two_sum([-1,0,1,2,-1,-4]))
    print(three_sum_using_two_sum([0,1,1]))