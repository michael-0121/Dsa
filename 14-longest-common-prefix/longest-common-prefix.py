class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x=strs[0]
        for i in strs[1::]:
            l=len(x)
            while x!=i[:l]:
                l-=1
                x=x[:l]
        return x