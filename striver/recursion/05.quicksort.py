class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """
            partition given array based on pivot which will be at correct position at the end of first function call
            repetitively partition array to the left and right of pivot and sort the array
        """
        self.quickSort(nums,0,len(nums)-1)
        return nums
    
    def partition(self,array, low, high):
        # Choose the rightmost element as pivot
        import random
        p=random.randint(low,high)
        array[p],array[high]=array[high],array[p]
        pivot = array[high]
        # Pointer for greater element (here i=-1)
        i = low - 1

        # Traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if array[j] <= pivot:
                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1
                # Swapping element at i with element at j
                (array[i], array[j]) = (array[j], array[i])

        #at the end of for loop variable i holds index of largest of smaller elements than pivot
        # Swap the pivot element with the greater element specified by i
        (array[i + 1], array[high]) = (array[high], array[i + 1])

        # Return the position from where partition is done
        return i + 1

# Function to perform quicksort
    def quickSort(self,array, low, high):
        if low < high:
            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = self.partition(array, low, high)

            # Recursive call on the left of pivot
            self.quickSort(array, low, pi - 1)

            # Recursive call on the right of pivot
            self.quickSort(array, pi + 1, high)

if __name__=="__main__":
    print(Solution().sortArray([5,4,3,2,1]))