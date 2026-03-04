class Solution:
    def factorial(self, n):

        factorial_answer = 1

        for i in range(1,n+1):
            factorial_answer *= i
        
        return factorial_answer