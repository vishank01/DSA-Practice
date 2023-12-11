class SubSets:
    def subsets(self,nums,target):
        cache = [[None for _ in range(target+1)] for _ in range(len(nums)+1)]
        for i in range(len(nums)+1):
            for j in range(target+1):
                if i==0 or j==0:
                    cache[i][j]=[]
        for i in range(1,len(nums)+1):
            for j in range(target+1):
                if nums[i-1]<=j:
                    p1 = cache[i-1][j-nums[i-1]] + [nums[i-1]]
                    p2 = cache[i-1][j]
                    cache[i][j] = p1 if len(p1)>len(p2) else p2
                else:
                    cache[i][j] = cache[i-1][j]
        return cache[i][j]

class EqualSubsetSum:
    def canPartition(self, nums):
        total_sum = sum(nums)
        if total_sum%2!=0:
            return False
        else:
            target = total_sum//2
            cache = [[None for _ in range(target+1)] for _ in range(len(nums)+1)]
            for j in range(target+1):
                if j==0:
                    cache[0][j]=False
            for i in range(len(nums)+1):
                if i==0:
                    cache[i][0]=True
            for i in range(1,len(nums)+1):
                for j in range(target+1):
                    if nums[i-1]<=j:
                        cache[i][j] = cache[i-1][j-nums[i-1]] or cache[i-1][j]
                    else:
                        cache[i][j] = cache[i-1][j]
        return cache[i][j]
    
print(SubSets().subsets([1,5,11,5],11))