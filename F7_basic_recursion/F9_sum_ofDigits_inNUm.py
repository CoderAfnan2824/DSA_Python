class Solution:
    def addDigits(self, num):
        #your code goes here

        if num == 0:
            return 0
        
        num = num % 10 + self.addDigits(num//10)
        return num % 10 + self.addDigits(num//10)