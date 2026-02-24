class Solution:
    def largestDigit(self, n):

        temp = n
        largestDigit = 0

        while temp > 0:

            largestDigit = max(largestDigit, temp % 10)
            temp //= 10
        
        return largestDigit