"""
Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
"""

def brute_force_approach(array:list[int],k:int):
    """Brute force approach
        if k=5, then valid i values are 
            i=0;i+5<=len(array);i++ 
                    or 
            i=0;i+5<len(array)+1;i++
                    or
            i=0;i<len(array)-5+1;i++

    Time complexity: O(N*K) 
        Since for every element of the input array, we are calculating the sum of its next ‘K’ elements, the time complexity of the above algorithm will be O(N*K) 
        where ‘N’ is the number of elements in the input array.Time complexity: Since for every element of the input array, we are calculating the sum of its next ‘K’ elements, 
        the time complexity of the above algorithm will be O(N*K) where ‘N’ is the number of elements in the input array.
    
    >>> brute_force_approach()
    [2.2, 2.8, 2.4, 3.6, 2.8]
    """
    output = []
    for i in range(0,len(array)-k+1):
        sum=0
        for j in range(i,i+k):
            sum+=array[j]
        output.append(sum/5)
    print(output)

# sliding window protocol
def sliding_window_approach(array:list[int],k:int):
    """Can we find a better solution? Do you see any inefficiency in the above approach?
    The inefficiency is that for any two consecutive subarrays of size ‘5’, the overlapping part 
    (which will contain four elements) will be evaluated twice. For example, take the above-mentioned input:

    The efficient way to solve this problem would be to visualize each contiguous subarray as a sliding window of ‘5’ elements. 
    This means that we will slide the window by one element when we move on to the next subarray. 
    To reuse the sum from the previous subarray, we will subtract the element going out of the window and add the element now being included in the sliding window. This will save us from going through the whole subarray to find the sum and, as a result, the algorithm complexity will reduce to O(N).
    
    >>> sliding_window_approach()
    [2.2, 2.8, 2.4, 3.6, 2.8]
    """
    sum = 0
    output = []
    for i in range(len(array)):
        #add all elements until window size is reached, once it is reached, maintain it
        if i<k:
            sum+=array[i]
        else:
            #subtract outgoing element and add incoming element
            sum=sum-array[i-k]+array[i]
        #add to output only if i cross k (in this case sum will have all k elements)
        if i>=k-1:
            output.append(sum/k)
    print(output)
    
if __name__=="__main__":
    sliding_window_approach(array=[1, 3, 2, 6, -1, 4, 1, 8, 2],k=5)