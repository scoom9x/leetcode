class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        smallest = 50
        second_smallest = 50
        
        for i in range(1, len(nums)):
            if nums[i] < smallest:
                second_smallest = smallest
                smallest = nums[i]
            elif nums[i] < second_smallest:
                second_smallest = nums[i]
        return nums[0] + smallest + second_smallest