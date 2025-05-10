class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {"I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        res = 0

        for i in range(0,len(s)):
            if i+1 < len(s) and rom[s[i]] < rom[s[i+1]]:
                res -= rom[s[i]]
            else:
                res += rom[s[i]]
        return res