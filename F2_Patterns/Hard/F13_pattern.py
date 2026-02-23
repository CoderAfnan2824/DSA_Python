class Solution:
    def pattern13(self, n):

        counter = 1
        for i in range(n):
            for j in range(i+1):
                print(counter,end=" ")
                counter += 1
            print()
