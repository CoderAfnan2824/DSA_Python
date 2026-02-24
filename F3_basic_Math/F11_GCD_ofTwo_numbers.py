class Solution:
    def GCD(self, n1, n2):

#       min_n = lambda n1,n2 : n1 if n1 > n2 else n2
#       value = min_n(n1,n2)

        if n1 <= n2:
            value = n1
        else:
            value = n2

        for i in range(value,1,-1):

            if n1 % i == 0 and n2 % i == 0:
                return i 
        
        return 1