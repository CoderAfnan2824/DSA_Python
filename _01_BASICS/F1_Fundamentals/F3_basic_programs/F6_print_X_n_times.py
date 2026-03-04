class Solution:
    def printX(self, X, N):

        for i in range(N):
            if i == N-1:
                print(X)
            else:
                print(X, end=" ")
        print()