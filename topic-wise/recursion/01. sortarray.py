def sortarray(arr:list):
    if len(arr)<=1:
        return arr
    else:
        return insert(sortarray(arr[:-1]),arr[-1])
        
def insert(arr:list,ele):
    if len(arr)==0 or arr[-1]<=ele:
        return arr+[ele]
    else:
        return insert(arr[:-1],ele)+[arr[-1]]
    
print(sortarray([15,12,52,0,-1,4,5,2]))