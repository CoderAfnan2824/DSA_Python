class Solution:
    def primeUptoN(self, n):

        counter = 0
        if n < 2:
            return counter
        
        for i in range(2,n+1):
            if self.isPrime(i):
                counter += 1
            
        return counter

    def isPrime(self, n):

            if n < 2:
                return False 

            for i in range(2, int(n ** 0.5)+1):

                if n % i == 0:
                    return False
            
            return True