class Solution:
    def LCM(self, n1, n2):

        if n1 >= n2:
            value = n1
        else:
            value = n2
        
        while True:

            if value % n1 == 0 and value % n2 == 0:
                break
            else:
                value += 1
        
        return value