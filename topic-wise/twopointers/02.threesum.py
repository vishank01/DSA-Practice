"""
https://leetcode.com/problems/3sum/

Problem Statement: Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

"""

def three_sum(nums:list[int])->set[tuple[int]]:
    """
        Approach:
            i+start+end=0
            start+end=-i
            Now use Two pointer Approach with target value -end

        Complexity:  
            Sorting the array will take O(N * logN). The searchPair() function will take O(N). As we are calling searchPair() for every number in the input array, this means that overall searchTriplets() will take O(N * logN + N^2), which is asymptotically equivalent to O(N^2).
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