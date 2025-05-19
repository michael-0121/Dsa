class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len (needle)
        if n == 0:
            return -1

        for i in range (00 , len(haystack)-n +1):
            if haystack[i :i+n] == needle:
                return i
        return -1