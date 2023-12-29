"""
Problem Statement:
    Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
    The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
    frequency
    of at least one of the chosen numbers is different.

    The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

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

"""
def combination_sum_recursion(candidates: list[int], target: int) -> list[list[int]]:

    def helper(candidates:list[int],n:int,target:int,output:list[list]|None = None)->list[list[int]]:
        if output is None:
            output = []
        if target==0:
            return [output]
        elif n==0 or target<0:
            return []
        else:
            if candidates[n-1]<=target:
                return helper(candidates,n,target-candidates[n-1],[candidates[n-1]]+output)+helper(candidates,n-1,target,output)
            else:
                return helper(candidates,n-1,target,output)
    
    return helper(candidates,len(candidates),target)

# def combination_sum_memoization(candidates: list[int], target: int) -> list[list[int]]:
#     n = len(candidates)
#     dp = [[None for _ in range(target+1)] for _ in range(n+1)]

#     def helper(candidates:list[int],n:int,target:int,output:list[list]|None = None)->list[list[int]]:
#         if dp[n][target]!=None:
#             print(n,target,dp[n][target])
#             # return dp[n][target]
#         if output is None:
#             output = []
#         if target==0:
#             return [output]
#         elif n==0 or target<0:
#             return []
#         else:
#             if candidates[n-1]<=target:
#                 dp[n][target] = helper(candidates,n,target-candidates[n-1],[candidates[n-1]]+output)+helper(candidates,n-1,target,output)
#             else:
#                 dp[n][target] = helper(candidates,n-1,target,output)
#             return dp[n][target]
    
#     a = helper(candidates,n,target)
#     return a

if __name__=="__main__":
    print(combination_sum_recursion([2,3,6,7], target = 7))
    print(combination_sum_recursion([2,3,5], target = 8))
    print(combination_sum_recursion(candidates = [2], target = 1))