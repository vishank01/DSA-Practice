"""
Problem Statement:
    Min Heap Construction
        array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41] 
        output = [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48, 87]
    
Parent Child Relationship:
    parent child relationship for parent i is child1 = 2*i+1 and child2 = 2*i+2
    so given any child, parent can be obtained by (child_idx-1)//2
    last child is n-1 so n-1=2*i+1
    => n = 2*i+2

Naive Approach:  
    To solve the problem follow the below idea:
        1. To build a Max-Heap from the given array elements might not necessarily follow the Heap property. 
        2. So, the idea is to heapify the complete binary tree formed from the array in reverse level order(bottom to top and right to left) following a top-down approach. 
        3. That is first heapify, the last node in level order traversal of the tree, then heapify the second last node and so on. 

Efficient Approach:
    To solve the problem using this approach follow the below idea:
        1. The above approach can be optimized by observing the fact that the leaf nodes need not to be heapified as they already follow the heap property. 
        2. Also, the array representation of the complete binary tree contains the level order traversal of the tree. 
        3. So the idea is to find the position of the last non-leaf node and perform the heapify operation of each non-leaf node in reverse level order.

Time Complexity Analysis: 
    1. Heapify a single node takes O(log N) time complexity where N is the total number of Nodes. 
    2. Therefore, building the entire Heap will take N heapify operations and the total time complexity will be O(N*logN).
    Note: 
        In reality, building a heap takes O(n) time depending on the implementation which can be seen

"""
class MinHeap:

    def heappush(self,heap:list[int],ele:int)->list[int]:
        heap.append(ele)
        self.sift_up(heap,len(heap)-1)

    def heapify(self,heap:list[int])->None:
        last_non_leaf_node_idx = (len(heap)-1-1)//2
        #now perform reverse level order traversal (bottom to top and then right to left side in array)
        for parent_idx in range(last_non_leaf_node_idx,-1,-1):
            self.sift_down(heap,parent_idx)

    def sift_up(self,heap:list[int],idx:int)->None:
        parent_idx = (idx-1)//2
        while parent_idx>0 and heap[parent_idx]>heap[idx]:
            heap[parent_idx],heap[idx] = heap[idx],heap[parent_idx]
            idx = parent_idx
            parent_idx = (idx-1)//2

    def sift_down(self,heap:list[int],idx:int)->None:
        child1_idx = 2*idx+1
        child2_idx = 2*idx+2
        smallest_idx = idx
        if child1_idx<len(heap) and heap[child1_idx]<heap[smallest_idx]:
            smallest_idx = child1_idx
        if child2_idx<len(heap) and heap[child2_idx]<heap[smallest_idx]:
            smallest_idx = child2_idx

        if smallest_idx!=idx:
            heap[smallest_idx],heap[idx] = heap[idx],heap[smallest_idx]
            idx = smallest_idx
            self.sift_down(heap,smallest_idx)
    
    def peek(self,heap:list[int])->int|None:
        return heap[0] if heap else None
    
    def remove(self,heap:list[int])->int:
        heap[0],heap[-1]=heap[-1],heap[0]
        min_val = heap.pop()
        self.sift_down(heap,0)
        return min_val

    def insert(self,heap:list[int],ele:int)->None:
        heap.append(ele)
        self.sift_up(heap,len(heap)-1)
    

if __name__=="__main__":
    min_heap = MinHeap()
    arr = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
    min_heap.heapify(arr)
    print(arr)