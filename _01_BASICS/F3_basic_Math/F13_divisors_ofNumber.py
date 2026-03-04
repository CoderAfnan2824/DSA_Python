class Solution:
    def divisors(self, n):

        ls = []
        
        for i in range(1,n+1):

            if n % i == 0:
                ls.append(i)
        
        return ls