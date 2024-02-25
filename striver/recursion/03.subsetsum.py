
def print_all_subsets_with_sum_k(array:list[int],k:int):
    subset = []
    def helper(array:list[int],n:int,k:int,subset:list[int]):
        if k==0:
            print(subset)
        elif n>0:
            if array[n-1]<=k:
                helper(array,n-1,k-array[n-1],subset+[array[n-1]])
            helper(array,n-1,k,subset)
    return helper(array,len(array),k,subset)

def count_all_subsets_with_sum_k(array:list[int],k:int):
    def helper(array:list[int],n:int,k:int,cnt=0):
        if k==0:
            return cnt+1
        elif n>0:
            if array[n-1]<=k:
                cnt = helper(array,n-1,k-array[n-1],cnt)
            cnt = helper(array,n-1,k,cnt)
        return cnt
    return helper(array,len(array),k)

def print_all_subsets_with_sum_k_backtracking(array:list[int],k:int):
    subset = []
    def helper(array:list[int],n:int,k:int,subset:list[int]):
        if k==0: print(subset)
        elif n>0:
            k-=array[n-1]
            subset.append(array[n-1])
            helper(array,n-1,k,subset)
            k+=array[n-1]
            subset.pop()
            helper(array,n-1,k,subset)
    return helper(array,len(array),k,subset)


if __name__=="__main__":
    print_all_subsets_with_sum_k([1,2,1],2)
    print_all_subsets_with_sum_k_backtracking([1,2,1],2)
    print(count_all_subsets_with_sum_k([1,2,1,],2))