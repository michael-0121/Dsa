class Solution:
    def canJump(self, nums: List[int]) -> bool:
        tar = len(nums)-1

        for i in range (len(nums)-1,-1,-1):
            if i + nums [i] >= tar:
                tar = i

        if tar == 0:
            return True 
        else:
            return False