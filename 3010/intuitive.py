class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        firstIdx = nums[0]
        nums.pop(0)
        nums.sort()
        
        return firstIdx + nums[0] + nums[1]

        
            