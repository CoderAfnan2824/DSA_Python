class Solution:
    def countOddDigit(self, n):

        temp = n
        no_of_digits = 0

        while temp > 0:
            
            digit = temp % 10
            if digit % 2 != 0:
                no_of_digits += 1
            temp //= 10
        
        return no_of_digits