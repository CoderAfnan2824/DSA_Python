class Solution:
    def NnumbersSum(self, N):
        #your code goes here

        if N == 1:
            return 1
        
        return N + self.NnumbersSum(N-1)