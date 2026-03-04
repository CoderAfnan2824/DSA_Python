class Solution:
    def pattern22(self, n):
        top = 0
        bottom = 2*n-1

        left = 0
        right = 2*n - 1
        
        for i in range(2*n-1):
            for j in range(2*n-1):
                
                top = i
                bottom = 2*n - i - 2

                left = j
                right = 2*n - j - 2

                print(n-min(top, bottom, left, right),end=" ")
            
            print()