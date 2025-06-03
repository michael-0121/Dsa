class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {")":"(","]":"[","}":"{"}
        sta =[]
        for i in range (0, len(s )):
            if len(sta) == 0:
                sta.append(s[i])
            elif s[i] in dictionary and sta[-1] == dictionary[s[i]]:
                sta.pop()
            else:
                sta.append (s[i])
        if len(sta) == 0:
            return True
        else :
            return False