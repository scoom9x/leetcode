class Solution:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        
        # Pass 1: Prefix products
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            
        # Pass 2: Suffix products
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res
