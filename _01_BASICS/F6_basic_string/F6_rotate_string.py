class Solution:    
    def rotateString(self, s, goal):
        #your code goes here

        if len(s) < len(goal):
            return False
        double_string = s + s 
        
        return goal in double_string