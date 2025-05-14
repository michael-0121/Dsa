class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers_found = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numbers_found:
                return [numbers_found[complement], i]
            numbers_found[nums[i]] = i
        return None
