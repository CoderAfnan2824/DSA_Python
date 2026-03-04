class Solution:
    def bubbleSort(self, nums):

        n = len(nums)

        for i in range(n-1):
            flag = True
            for j in range(n-1-i):

                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    flag = False
            
            if flag == True:
                return nums
        
        return nums