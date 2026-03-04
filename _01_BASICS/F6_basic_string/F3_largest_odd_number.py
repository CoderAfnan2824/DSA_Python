class Solution:  
    def largeOddNum(self, s: str) -> str:
        #your code goes here

        last_index = len(s) - 1
        start_index = 0

        while last_index >= 0  and int(s[last_index]) % 2 ==0:
            last_index -= 1

        while start_index < len(s) and s[start_index] == '0':
            start_index += 1
        
        
        return s[start_index:last_index+1]
