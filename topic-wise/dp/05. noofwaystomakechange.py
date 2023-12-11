def numberOfWaysToMakeChange(n, denoms):
    return changeHelper(denoms,len(denoms),n)

def changeHelper(denoms,n,target):
    t=[[0 for i in range(target+1)] for _ in range(n+1)]
    for j in range(1,target+1):
        t[0][j] = 0
    for i in range(n+1):
        t[i][0] = 1
    for i in range(1,n+1):
        for j in range(1,target+1):
            if denoms[i-1]<=target:
                 t[i][j] = t[i][j-denoms[i-1]]+t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
            print(i,j,t[i][j])
    return t[n][target]
        
def numberOfWaysToMakeChange(n, denoms):
    return changeHelper(denoms,len(denoms),n)

def changeHelper(denoms,n,target):
    if target==0:
        return 1
    elif n==0:
        return 0
    elif denoms[n-1]<=target:
        return changeHelper(denoms,n,target-denoms[n-1])+changeHelper(denoms,n-1,target)
    else:
        return changeHelper(denoms,n-1,target)
        

print(numberOfWaysToMakeChange(6,[1,5],))