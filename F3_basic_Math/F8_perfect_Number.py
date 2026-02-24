class Solution:
    def isPerfect(self, n: int) -> bool:

        summ = 0
        for i in range(1,n):
            if n % i == 0:
                summ += i
        
        return summ == n