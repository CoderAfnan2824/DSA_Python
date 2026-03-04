class Solution:
    def reverseString(self,s):
        #your code goes here
        
        self.my_reverse(0,len(s)-1,s)
        return s
        
    
    def my_reverse(self,i,j,s):

        if i >= j:
            return

        s[i], s[j] = s[j], s[i]
        self.my_reverse(i+1, j-1, s)
