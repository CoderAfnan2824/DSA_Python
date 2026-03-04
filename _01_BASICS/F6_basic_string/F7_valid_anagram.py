class Solution:    
    def anagramStrings(self, s, t):
        #your code goes here
        if len(s) != len(t):
            return False
        hash_code = [0]*26

        n = len(s)

        for i in range(n):
            hash_code[ord(s[i])-ord('a')] += 1
            hash_code[ord(t[i])-ord('a')] -= 1
        
        for i in hash_code:
            if i != 0:
                return False 
        
        return True