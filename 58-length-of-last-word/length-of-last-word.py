class Solution(object):
    def lengthOfLastWord(self, s):
        word = len(s.split()[-1])
         
        return word