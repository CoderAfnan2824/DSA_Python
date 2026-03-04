class Solution:
    def pattern9(self, n):

        self.pattern7(n)
        self.pattern8(n)

    
    def pattern7(self, n):

        for i in range(n):

            for j in range(n-i-1):
                print(" ",end="")

            for j in range(2*i+1):
                print('*',end="")
            print()

    def pattern8(self, n):

        for i in range(n):

            for j in range(i):
                print(' ',end="")
            
            for j in range(2*(n-i)-1):
                print('*',end="")
            print()