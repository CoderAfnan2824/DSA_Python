class Solution:
    def isSorted(self, nums):
        
        if len(nums) <= 1:
            return True

        def check_sort(i,nums):

            n = len(nums)

            if i == n:
                return True
            
            if nums[i] < nums[i-1]:
                return False
            
            return check_sort(i+1, nums)
        
        return check_sort(1,nums)
