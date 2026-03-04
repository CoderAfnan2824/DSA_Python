class Solution:
    def frequencySort(self, s):
        #your code goes here

        #creat list of tuples where each tuple contain default value and a character till 26
        freq = [(0, chr(i + ord('a'))) for i in range(26)]

        for ch in s:
            index = ord(ch)-ord('a')

            #freq[index][0] = freq[index][0] + 1
            #above commented line doesn't work as tuple is unchangable, so we assign new value to index of list everytime we find the character 
            freq[index] = (freq[index][0]+1,ch)

        #x[0] is frequency, x[1] is character 
        #x: -x[0] means sort based on frequency in descending order
        #x: x[0],x[1] sort in ascending on frequency, then on character 
        freq.sort(key = lambda x: (-x[0],x[1]))

        #it store only the character list 
        result = [ch for f,ch in freq if f > 0]
        
        return result