class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lis = []
        
        for i in range(len(nums)):
            otherNumber = target - nums[i]
            nums2 = nums.copy()
            nums2[i] = None
            if otherNumber in nums2:
                lis.append(i)
                lis.append(nums2.index(otherNumber))
                break
        return lis

