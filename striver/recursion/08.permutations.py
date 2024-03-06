def permutations_of_string_using_swap(string:str):
    """As python strings are mutable, it is converted to list to use swapping technique
    """
    def permutation_helper(string:list[str],low:int,high:int):
        if low==high: print("".join(string))
        for i in range(low,high):
            string[i],string[low]=string[low],string[i]
            permutation_helper(string,low+1,high)
            string[i],string[low]=string[low],string[i]
    permutation_helper(list(string),0,len(string))

def permutations_of_string_using_hash_maps(string:str):
    """maps are used to track indexes of elements that are already considered in output which avoids need for swap"""
    def permutations_helper(string:str,low:int,high:int,maps:set[int],out=""):
        if low==high: print(out)
        else:
            for i in range(high):
                if i not in maps:
                    maps.add(i)
                    out+=string[i]
                    permutations_helper(string,low+1,high,maps,out)
                    out=out[:-1]
                    maps.remove(i)
    permutations_helper(string,0,len(string),set())

if __name__=="__main__":
    # permutations_of_string_using_swap("abc")
    permutations_of_string_using_hash_maps("efg")