class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums)-1:
            further = 0
            for i in range (l ,r+1):
                further = max (further, nums[i]+i)
            l = r
            r = further
            res += 1

        return res