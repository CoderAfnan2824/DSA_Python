class Solution:
    def mostFrequentElement(self, nums):

        max_element = 0

        for i in nums:
            max_element = max(max_element, i)

        hash = [0] * (max_element + 1)

        for i in nums:
            hash[i] += 1
        
        max_count = 0
        element = 0
        for i in range(max_element+1):
            if hash[i] > max_count:
                max_count = hash[i]
                element = i 
            elif hash[i] == max_count:
                element = min(element, i)
        
        return element


     