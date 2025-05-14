class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic = {}
        counter = 0 
        for i in range (0,len(nums)):
            if nums[i] not in dic.keys():
                nums[counter] = nums[i]
                counter += 1
                dic[nums[i]] = 1
        return counter