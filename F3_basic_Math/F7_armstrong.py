class Solution:
    def isArmstrong(self, n):

        no_of_digits = self.countDigit(n)
        #print(no_of_digits)
        armstrong_sum = 0
        temp = n

        for i in range(no_of_digits):
            digit = temp % 10
            temp //= 10

            armstrong_sum += digit ** no_of_digits
        
        return armstrong_sum == n
    def countDigit(self, n):

        if n == 0:
            return 1

        temp = n
        no_of_digits = 0

        while temp > 0:
            temp //= 10
            no_of_digits += 1
        
        return no_of_digits