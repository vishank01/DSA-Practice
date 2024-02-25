class MergeSort:
    def sort_array(self, nums: list[int]) -> list[int]:
        return self.merge_sort_helper(nums,0,len(nums)-1)

    def merge_sort_helper(self,nums,low,high):
        if low>=high: return [nums[low]]
        mid = (low+high)//2
        left_array = self.merge_sort_helper(nums,low,mid)
        right_array = self.merge_sort_helper(nums,mid+1,high)
        return self.merge_sorted_arrays(left_array,right_array)

    def merge_sorted_arrays(self,arr1,arr2):
        n1 = len(arr1)
        n2 = len(arr2)
        arr = [];i=0;j=0
        while i+j<n1+n2:
            if i<n1 and j<n2:
                if arr1[i]<=arr2[j]:
                    arr.append(arr1[i]);i+=1
                else:
                    arr.append(arr2[j]);j+=1
            elif i<n1:
                arr.append(arr1[i]);i+=1
            else:
                arr.append(arr2[j]);j+=1
        return arr
    
if __name__=="__main__":
    print(MergeSort().sort_array([5,4,3,2,1]))