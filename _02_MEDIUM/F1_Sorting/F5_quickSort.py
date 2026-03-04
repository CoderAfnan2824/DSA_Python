'''

we can have two types of partition in quick sort :

Lomuto Partition Scheme:
    •    Pivot is usually chosen as the last element.
    •    Maintains a boundary index for elements smaller than or equal to pivot.
    •    Scans array once from left to right.
    •    After traversal, pivot is placed in its correct sorted position.
    •    Simple and easy to implement.
    •    Performs more swaps.
    •    Works well for understanding basics but slightly less efficient in practice.

Hoare Partition Scheme:
    •    Pivot is usually chosen as the first element.
    •    Uses two pointers moving inward from both ends.
    •    Swaps elements that are on the wrong side of pivot.
    •    Returns a partition index; pivot may not end at exact sorted position immediately.
    •    Performs fewer swaps.
    •    Generally faster and more efficient than Lomuto.
    •    Slightly trickier to implement correctly.

Time Complexity (both):
    •    Average: O(n log n)
    •    Worst case: O(n²) (when pivot choice is poor)

Use Lomuto for simplicity.
Use Hoare for better performance and fewer swaps.
'''
class Solution:
    def quickSort(self, nums):

        self.qs(nums, 0, len(nums)-1)
        return nums 

    def qs(self, nums, low, high):

        #divide array until there is only one element
        if low < high:
        
        #obtain current point where we fix pivot
            pivot = self.partition(nums, low, high)
        
        #perform quick sort again on left part and right part from pivot
            self.qs(nums, low, pivot - 1)
            self.qs(nums, pivot + 1, high)
        

    def partition(self, nums, low, high):

#Lomuto Partition: Setting starting element as
        pivot = nums[low]

        i = low + 1
        j = high 

        while True:

            #make sure i to go till high else it results in infinite loop in [2,3] case 
            while i <= high and nums[i] <= pivot:
                i += 1
            
            
            while j >= low and nums[j] > pivot:
                j -= 1
            
            if j < i:
                break
            
            nums[i], nums[j] = nums[j], nums[i]
        
        nums[j], nums[low]  = nums[low], nums[j] 

        return j

