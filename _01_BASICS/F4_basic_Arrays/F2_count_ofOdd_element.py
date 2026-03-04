class Solution:
    def countOdd(self, arr, n):
        # Your code goes here
        odd_count = 0

        for i in arr:
            if i % 2 == 1:
                odd_count += 1
        
        return odd_count