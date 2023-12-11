class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1 and k==1:
            return 0
        else:
            mid = 2**(n-2)
            if k<=mid:
                return self.kthGrammar(n-1,k)
            else:
                return self.kthGrammar(n-1,k-mid)^1

print(Solution().kthGrammar(6,3))