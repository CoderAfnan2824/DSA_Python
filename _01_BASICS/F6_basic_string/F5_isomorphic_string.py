class Solution:
    def isomorphicString(self, s : str, t : str) -> bool:
        #your code goes here

        s_hash = [0] * 26
        t_hash = [0] * 26

        n = len(s)

        for i in range(n):
            if s_hash[ord(s[i])-ord('a')] != t_hash[ord(t[i])-ord('a')]:
                return False
            # i + 1 will avoid zero as relation as its already setup initially
            s_hash[ord(s[i])-ord('a')] = i + 1
            t_hash[ord(t[i])-ord('a')] = i + 1

        return True