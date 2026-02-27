class Solution:
    def reverseArray(self, nums):
        #your code goes here

        def reverse_arr(i, j, nums):
            if i >= j:
                return 
            
            nums[i], nums[j] = nums[j], nums[i]

            reverse_arr(i+1, j-1, nums)
        
        reverse_arr(0, len(nums)-1, nums)
        return nums