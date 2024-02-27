"""
Problem Statement: Given an array print all the sum of the subset generated from it, in the increasing order.

Example 1:

    Input: N = 3, arr[] = {5,2,1}
    Output: 0,1,2,3,5,6,7,8
    Explanation: We have to find all the subset's sum and print them
    In this case the generated subsets are [ [], [1], [2], [2,1], [5], [5,1], [5,2]. [5,2,1],so the sums we get will be  0,1,2,3,5,6,7,8

Time Complexity: 
    O(2^n)+O(2^n log(2^n)). 
    Each index has two ways. You can either pick it up or not pick it. 
    So for n index time complexity for O(2^n) and for sorting it will take (2^n log(2^n)).

Space Complexity: 
    O(2^n) for storing subset sums, since 2^n subsets can be generated for an array of size n.
"""

def subsets_with_all_sums(nums:list[int]):
    def helper(nums:list[int],n:int,ans:list[int],n_sum:int=0):
        if n==0: ans.append(n_sum)
        else:
            helper(nums,n-1,ans,n_sum+nums[n-1])
            helper(nums,n-1,ans,n_sum)

    ans = []
    helper(nums,len(nums),ans)
    ans.sort()
    return ans

class Solution:
    def unique_subsets_with_duplicated_numbers(self,nums):
        # write the code  logic here !!!
        ans = []
        self.helper(nums,0,len(nums),ans,ds=[]) 
        return ans

    def helper(self,nums,idx,n,ans,ds):
        ans.append(ds.copy())
        for i in range(idx,n):
            if i>idx and nums[i-1]==nums[i]: continue
            ds.append(nums[i])
            self.helper(nums,i+1,n,ans,ds)
            ds.pop()

if __name__=="__main__":
    print(subsets_with_all_sums([1,2,3]))
    print(Solution().unique_subsets_with_duplicated_numbers([1,2,3]))