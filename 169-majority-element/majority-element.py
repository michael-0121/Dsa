class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majo = len(nums)//2

        for eh in set (nums):
            if nums.count(eh)>majo:
                return eh