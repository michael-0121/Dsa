class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = 0
        maxstring = 0
        dictx= {}
        for i in range (0,len(s)):
            while s[i] in dictx.keys():
                del dictx[s[j]]
                j += 1
            maxstring = max(maxstring, i- j +1)
            dictx[s[i]] = 1
        return maxstring 