"""
Pattern Used: Pick/Not Pick element from array in recursion

https://www.youtube.com/watch?v=OyZFFqQtu98&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=10&pp=iAQB

Problem Statement: Combination Sum
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

You may return the combinations in any order.

Example 1:

    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
        2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
        7 is a candidate, and 7 = 7.
        These are the only two combinations.

Example 2:

    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

    Input: candidates = [2], target = 1
    Output: []

Constraints:

    1 <= candidates.length <= 30
    2 <= candidates[i] <= 40
    All elements of candidates are distinct.
    1 <= target <= 40

Time Complexity: 
    k*(2^t) where t is target amount(until target is reached, recursion won't stop) 
    and k is average length of every data structure (copying ds to ans)
Space Complexity: 
    k*x where x is x combinations

If repetition is not allowed then Time Complexity would be (2^n) 2 choices for every n
"""

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        return self.helper(candidates,len(candidates),target,[])

    def helper(self,candidates:list[int],n:int,target:int,out:list[int]):
        if n==0 or target==0:
            return [out] if target==0 else []
        if candidates[n-1]<=target:
            output = self.helper(candidates,n,target-candidates[n-1],out+[candidates[n-1]])+\
                    self.helper(candidates,n-1,target,out)
        else:
            output = self.helper(candidates,n-1,target,out)
        return output
    
class PassbyRefernceSolution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        self.helper(candidates,len(candidates),target,ans,ds=[])
        return ans

    def helper(self,candidates:list[int],n:int,target:int,ans:list[list[int]],ds:list[int]):
        if target==0: ans.append(ds.copy());return
        elif n==0: return
        if candidates[n-1]<=target:
            ds.append(candidates[n-1])
            self.helper(candidates,n,target-candidates[n-1],ans,ds)
            ds.pop()
        self.helper(candidates,n-1,target,ans,ds)
    
class BacktrackSolution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        self.helper(candidates,len(candidates),target,ans,[])
        return ans

    def helper(self,candidates:list[int],n:int,target:int,ans:list[list[int]],ds:list[int]):
        if n==0:
            if target==0: ans.append(ds.copy())
            return
        if candidates[n-1]<=target:
            ds.append(candidates[n-1])
            self.helper(candidates,n,target-candidates[n-1],ans,ds)
            ds.pop()
        self.helper(candidates,n-1,target,ans,ds)

if __name__=="__main__":
    print(PassbyRefernceSolution().combinationSum([2,3,5], target = 8))