class Solution:
    def arraySum(self, nums):
        #your code goes here
        n = len(nums) - 1
        if n == 0:
            return nums[0]

        return nums[n] + self.arraySum(nums[:n])