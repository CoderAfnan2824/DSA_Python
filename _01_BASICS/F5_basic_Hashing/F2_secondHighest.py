class Solution:
    def secondMostFrequentElement(self, nums):

        max_element = 0

        for i in nums:
            max_element = max(max_element, i)

        hash = [0] * (max_element + 1)

        for i in nums:
            hash[i] += 1
        
        max_count = 0
        element = -1

        second_max_count = 0
        second_element = -1

        for i in range(max_element+1):

            if hash[i] > max_count:
                second_max_count = max_count
                second_element = element 

                max_count = hash[i]
                element = i 
            elif hash[i] == max_count:
                element = min(element, i)
            elif hash[i] < max_count and hash[i] > second_max_count:
                second_max_count = hash[i]
                second_element = i 
            elif hash[i] == second_max_count:
                second_element = min(second_element, i)
        
        return second_element


     
