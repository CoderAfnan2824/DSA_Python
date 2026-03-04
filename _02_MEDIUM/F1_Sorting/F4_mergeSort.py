class Solution:
    def mergeSort(self, nums):
        low = 0
        high = len(nums)

        self._merge_sort_recursive(nums, low, high-1)
        return nums


    def _merge_sort_recursive(self, nums, low, high):

        if low >= high:
            return
        mid = (high + low ) // 2
        self._merge_sort_recursive(nums, low, mid)
        self._merge_sort_recursive(nums, mid+1, high)

        self._simple_merge(nums, low, mid, high)
    
    def _simple_merge(self,nums, low, mid, high):

        left = low 
        right = mid + 1
        index = 0 
        temp = [0] * ( high - low + 1 )
        while left <= mid and right <= high:

            if nums[left] <= nums[right]:
                temp[index] = nums[left]
                left += 1
                index += 1
            else:
                temp[index] = nums[right]
                right += 1
                index += 1

        while left <= mid:
            temp[index] = nums[left]
            left += 1
            index += 1
        
        while right <= high:
            temp[index] = nums[right]
            right += 1
            index += 1
        
        for i in range(low,high+1):
            nums[i] = temp[i-low]


    
    