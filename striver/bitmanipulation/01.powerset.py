def print_all_sub_sequences(array:list[int]):
    n = len(array)
    out = set()
    #1<<n is same as 2**n
    for num in range(1<<n):
        arr = []
        for i in range(n):
            #check if the ith bit in number is set or not
            if num &(1<<i):
                arr.append(array[i])
            out.add(tuple(arr))
    print(out)

if __name__=="__main__":
    print_all_sub_sequences([1,2,3])