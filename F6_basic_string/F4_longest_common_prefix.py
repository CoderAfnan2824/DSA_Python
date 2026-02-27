class Solution:  
    def longestCommonPrefix(self, strs) :
        #your code goes here

        if len(strs) <= 1:
            return strs[0]

        strs.sort()

        first = strs[0]
        last = strs[len(strs)-1]

        result = ""

        i  = 0
        while i < len(first) and i < len(last):
            if first[i] == last[i]:
                result += first[i]
            else:
                break
            i += 1

        return result