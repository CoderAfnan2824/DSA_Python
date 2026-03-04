class Solution:
    def reverseNumber(self, n):

        temp = n

        reverse = 0

        while temp > 0:

            reverse = reverse * 10 + temp % 10
            temp //= 10

        return reverse