class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j=0
        minlen = math.inf
        sumx = 0

        for i in range (0,len(nums)):
            sumx += nums[i]

            while sumx >= target:
                minlen = min (minlen,i-j+1)
                sumx -= nums[j]
                j += 1
        if minlen == math.inf:
            return 0
        else:
            return minlen