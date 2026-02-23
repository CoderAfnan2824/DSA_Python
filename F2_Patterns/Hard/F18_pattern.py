class Solution:
    def pattern18(self, n):

        for i in range(n):
            for j in range(n-i-1,n):
                print(chr(65+j),end=" ")
            print()