"""
    sample input [[1,2],[4,3],[5,6],[6,7]]
    capacity = 10

    o/p = [10,[1,3]]

    items =  [
    [465, 100],
    [400, 85],
    [255, 55],
    [350, 45],
    [650, 130],
    [1000, 190],
    [455, 100],
    [100, 25],
    [1200, 190],
    [320, 65],
    [750, 100],
    [50, 45],
    [550, 65],
    [100, 50],
    [600, 70],
    [240, 40]
  ]
capacity = 200
o/p = [1500,[3,12,14]]
"""

cache = []
items =  [
    [465, 100],
    [400, 85],
    [255, 55],
    [350, 45],
    [650, 130],
    [1000, 190],
    [455, 100],
    [100, 25],
    [1200, 190],
    [320, 65],
    [750, 100],
    [50, 45],
    [550, 65],
    [100, 50],
    [600, 70],
    [240, 40]
  ]
capacity = 200

def knapsackProblem(items,capacity):
    return kshelper(items,len(items),capacity)

def kshelper(items,n,c,val=0,idxs=None):
    if idxs is None:
        idxs = []
    if n==0 or c==0:
        return [val,idxs]
    else:
        _val,wt = items[n-1]
        if wt<=c:
            p1 = kshelper(items,n-1,c-wt,val+_val,idxs+[n-1])
            p2 = kshelper(items,n-1,c,val,idxs)
            return p1 if p1[0]>p2[0] else p2
        else:
            return kshelper(items,n-1,c,val,idxs)
        
print(knapsackProblem(items,capacity))

        
def knapsackProblem(items,capacity):
    return kshelper(items,len(items),capacity)

def kshelper(items,n,c,val=0,idxs=None):
    if idxs is None:
        idxs = []
    if n==0 or c==0:
        return [val,idxs]
    else:
        _val,wt = items[n-1]
        if wt<=c:
            p1 = kshelper(items,n-1,c-wt,val+_val,idxs+[n-1])
            p2 = kshelper(items,n-1,c,val,idxs)
            return p1 if p1[0]>p2[0] else p2
        else:
            return kshelper(items,n-1,c,val,idxs)