class Solution:
    def pattern11(self, n):

        for i in range(n):

            for j in range(i+1):
                summ = i + j
                if summ % 2 == 0:
                    print('1 ',end="")
                else:
                    print('0 ',end="")
            print()
            