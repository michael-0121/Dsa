class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        for each in nums:
            if each != val:
                nums[count] = each
                count += 1
        return count
