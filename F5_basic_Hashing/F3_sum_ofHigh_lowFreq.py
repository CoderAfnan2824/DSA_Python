class Solution:
    def sumHighestAndLowestFrequency(self, nums):
  
        max_element = 0

        for i in nums:
            max_element = max(max_element, i)

        hash = [0] * (max_element + 1)

        for i in nums:
            hash[i] += 1
        
        min_count, max_count = 10 ** 4, 0

        for i in hash:
            if i != 0:
                min_count = min(min_count,i)
                max_count = max(max_count, i)

        return min_count + max_count


     
