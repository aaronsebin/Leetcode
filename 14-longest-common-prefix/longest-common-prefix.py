class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        prefix = ""
        for i in range(len(min(strs, key=len))):
            current = strs[0][i]  #taking the first letter from the first word
        
            for s in strs[1:]:
                if s[i] != current:
                    return prefix
            
            prefix += current
            
        return prefix