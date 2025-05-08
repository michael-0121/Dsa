class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        num1 = len(s)
        num2 = len(t)

        if num1 == 0:
            return True 

        i=0
        j=0

        while j<num2 and i<num1:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        if i == num1:
            return True
        else:
            return False