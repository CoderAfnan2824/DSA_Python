class Solution:
    def checkPrime(self, num):
        #your code goes here
        if num < 2:
            return False

        def isPrime(i, num):

            if i * i > num:
                return True
            
            if num % i == 0:
                return False 
            
            return isPrime(i+1, num)
        
        return isPrime(2,num)