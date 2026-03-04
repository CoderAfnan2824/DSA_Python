class Solution:
    def countDigit(self, n):

        if n == 0:
            return 1

        temp = n
        no_of_digits = 0

        while temp > 0:
            temp //= 10
            no_of_digits += 1
        
        return no_of_digits

