class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ind = -1
        try:
            pre = strs [0][0]
        except:
            return ""
        try:
            for i in range (0, len (strs[0])):
                flag = True 
                for j in range(0, len(strs)):
                    if strs [j][i] != pre:
                        flag = False 
                        break 
                if flag :
                    ind += 1
                    pre = strs[0][ind +1]
                else:
                    break 
        except:
            return strs[0][:ind +1]
        if ind == -1:
            return ""
        else:
            return strs[0][:ind +1]