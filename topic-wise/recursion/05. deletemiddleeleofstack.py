def delmiddleele(arr:list,mid_idx):
    if len(arr)<=1:
        return []
    elif len(arr)==mid_idx:
        return arr[:-1]
    else:
        return delmiddleele(arr[:-1],mid_idx)
    
print(delmiddleele([15,12,52,0,-1,4,5,2,3]),4)