class Solution:
    def reverse(self, arr: list, n: int) -> None:

        for i in range(n//2):

            temp = arr[i]
            arr[i] = arr[n-i-1]
            arr[n-i-1] = temp 