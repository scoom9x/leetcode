class Solution(object):
    def sortColors(self, nums):
        r, w, b = 0, 0, 0
        for n in nums:
            if n == 0:
                r += 1
            elif n == 1:
                w += 1
            else:
                b += 1
                
        for i in range(len(nums)):
            if r > 0:
                nums[i] = 0
                r -= 1
            
            elif w > 0:
                nums[i] = 1
                w -= 1
            
            elif b > 0:
                nums[i] = 2
                b -= 1
        