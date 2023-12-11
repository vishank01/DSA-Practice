def unique_subset(ip,op="",res=None):
    if res is None:
        res=set()
    if len(ip)==0:
        res.add(op)
    else:
        unique_subset(ip[1:],op,res)
        unique_subset(ip[1:],op+ip[0],res)
    return res

def subset(ip,op=""):
    if len(ip)==0:
        print(op)
    else:
        subset(ip[1:],op)
        subset(ip[1:],op+ip[0])

print("subsets: "+str(subset("abb")))
print("Unique subsets: "+str(unique_subset("abb")))