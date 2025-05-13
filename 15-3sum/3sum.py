class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)
        n = len(nums)

        for k in range(0,n-2):
            i = k + 1
            j = n - 1

            temp = - nums[k]

            while i < j:
                tempin = nums[i] + nums[j]

                if tempin > temp:
                    j -= 1
                elif tempin < temp:
                    i += 1
                else:
                    res.add((nums[k], nums[i], nums[j]))
                    i += 1
                    j -= 1

        return list(res)