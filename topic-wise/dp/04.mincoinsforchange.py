#with recursion
def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    res = ks(denoms,len(denoms),n)
    return res if res!=float("inf") else -1

def ks(denoms,n,c):
    if n==0:
        return float('inf')
    elif c==0:
        return 0
    else:
        if denoms[n-1]<=c:
            return min(1+ks(denoms,n,c-denoms[n-1]),ks(denoms,n-1,c))
        else:
            return ks(denoms,n-1,c)


#top down
def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    cache = [[0 for _ in range(n+1)] for _ in range(len(denoms)+1)]
    for j in range(n+1):
        cache[0][j]=float('inf')
    for i in range(1,len(denoms)+1):
        for j in range(1,n+1):
            if denoms[i-1]<=j:
                cache[i][j] = min(cache[i][j-denoms[i-1]]+1,cache[i-1][j])
            else:
                cache[i][j] = cache[i-1][j]
    return cache[-1][-1] if cache[-1][-1]!=float('inf') else -1

print(minNumberOfCoinsForChange(7,[1,5,10,]))


