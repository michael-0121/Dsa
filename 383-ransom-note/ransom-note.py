class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictionary = {}
        for each in magazine:
            if each not in dictionary:
                dictionary[each] = 1
            else:
                dictionary[each] += 1

        for each in ransomNote:
            if each not in dictionary:
                return False
            elif dictionary[each]<1:
                return False 
            else:
                dictionary[each] -= 1
        return True
            