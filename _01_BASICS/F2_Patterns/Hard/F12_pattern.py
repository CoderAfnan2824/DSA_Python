class Solution:
    def pattern12(self, n):

        for i in range(n):

            for j in range(i+1):
                print(j+1,end="")
            
            for j in range(2*(n-i)-2):
                print(' ',end="")
            
            for j in range(i+1,0,-1):
                print(j,end="")
            
            print()