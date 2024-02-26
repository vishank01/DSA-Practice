"""
Pattern: loop with recursion  (this will avoid duplicate combinations in recursion)

https://youtu.be/G1fRTGRxXU8?list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&t=340
https://youtu.be/G1fRTGRxXU8?list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&t=1136

Problem Statement: CombinationSum2

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

    Input: candidates = [10,1,2,7,6,1,5], target = 8
    Output: 
    [
    [1,1,6],
    [1,2,5],
    [1,7],
    [2,6]
    ]

Example 2:

    Input: candidates = [2,5,2,1,2], target = 5
    Output: 
    [
    [1,2,2],
    [5]
    ]
 

Constraints:

    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30

Challenge:
    Output should not contain duplicate answers like [[1,1,2],[1,2,1],[2,1,1]] only one combination should be there
"""

class SolutionBruteforce:
    def combinationSum2(self, candidates: list[int], target: int) -> list[set[int]]:
        ans = set()
        self.helper(candidates,len(candidates),target,ans,ds=[])
        return list(ans)

    def helper(self,candidates:list[int],n:int,target:int,ans:set[set[int]],ds:list[int]):
        if target==0: ds.sort();ans.add(tuple(ds));return
        elif n==0: return
        if candidates[n-1]<=target:
            ds.append(candidates[n-1])
            self.helper(candidates,n-1,target-candidates[n-1],ans,ds)
            ds.pop()
        self.helper(candidates,n-1,target,ans,ds)

class SolutionUsingSubSets:
    def combinationSum2(self, candidates: list[int], target: int) -> list[set[int]]:
        ans = []
        candidates.sort()
        self.helper(candidates,0,len(candidates),target,ans,ds=[])
        return ans
    
    def helper(self,candidates:list[int],idx:int,n:int,target:int,ans:list[list[int]],ds:list[int]):
        if target==0: ans.append(ds.copy());return
        for i in range(idx,n):
            #skip elements starting with same element again to avoid duplicates
            #if i>idx then i-1 will start from idx otherwise it may exclude some data
            if i>idx and candidates[i-1]==candidates[i]: continue
            #array is sorted so next elements will also be greater than target
            if candidates[i]>target: break
            ds.append(candidates[i])
            self.helper(candidates,i+1,n,target-candidates[i],ans,ds)
            ds.pop()

if __name__=="__main__":
    print(SolutionUsingSubSets().combinationSum2([2,5,2,1,2], target = 5))