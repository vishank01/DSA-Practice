"""
    Problem Statement:
        write a function that takes in an array of atleast two integers and that returns an array
        of the starting and ending indices of smallest subarray in the input array that needs to be
        sorted in place in order for the entire input array to be sorted (in asc order)

        if the input array is already sorted, return [-1,-1]

    Sample Input:
        nums = [1,2,4,7,10,11,7,12,6,7,16,18,19]
        output: [3,9]
"""


def subarray_sort(nums:list[int])->int:
    """
        Approach:
            As we know, once an array is sorted (in ascending order), the smallest number is at the beginning and the largest number is at the end of the array. 
            So if we start from the beginning of the array to find the first element which is out of sorting order i.e., which is smaller than its previous element, and similarly from the end of array to find the first element which is bigger than its previous element, will sorting the subarray between these two numbers result in the whole array being sorted?
            
            Let’s try to understand this with the Example mentioned above. In the following array, what are the first numbers out of sorting order from the beginning and the end of the array:

            [1, 3, 2, 0, -1, 7, 10]
            
            Starting from the beginning of the array the first number out of the sorting order is 2 as it is smaller than its previous element which is 3.
            Starting from the end of the array the first number out of the sorting order is 0 as it is bigger than its previous element which is -1
            As you can see, sorting the numbers between 3 and -1 will not sort the whole array. To see this, the following will be our original array after the sorted subarray:

            [1, -1, 0, 2, 3, 7, 10]
            
            The problem here is that the smallest number of our subarray is -1 which dictates that we need to include more numbers from the beginning of the array to make the whole array sorted. 
            We will have a similar problem if the maximum of the subarray is bigger than some elements at the end of the array. To sort the whole array we need to include all such elements that are smaller than the biggest element of the subarray. 
            So our final algorithm will look like:

                1. From the beginning and end of the array, find the first elements that are out of the sorting order. The two elements will be our candidate subarray.
                2. Find the maximum and minimum of this subarray.
                3. Extend the subarray from beginning to include any number which is bigger than the minimum of the subarray.
                4. Similarly, extend the subarray from the end to include any number which is smaller than the maximum of the subarray.

    """
    n = len(nums)
    start,end = 0,n-1

    #find the first number out of sorting order from the end
    while start<n-1 and nums[start]<=nums[start+1]:
        start+=1

    if start==n-1: return [-1,-1]

    while end>0 and nums[end-1]<=nums[end]:
        end-=1

    min_ele,max_ele= float('inf'),float('-inf')
    #find the max and min of the subarray
    for i in range(start,end+1):
        min_ele = min(min_ele,nums[i])
        max_ele = max(max_ele,nums[i])

    #extend the subarray to include any number which is bigger than the minumum of the subarray
    while start >0 and nums[start-1] > min_ele:
        start-=1

    while end<n-1 and nums[end+1]<max_ele:
        end+=1
    
    return [start,end]


if __name__=="__main__":
    print(subarray_sort(nums = [2,2,2,1,1,1]))
    print(subarray_sort([1,2,4,7,10,11,7,12,6,7,16,18,19]))