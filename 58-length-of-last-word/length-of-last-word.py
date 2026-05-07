class Solution(object):
    def lengthOfLastWord(self, s):
        word = s.split()[-1]
        length = len(word) 
        return length