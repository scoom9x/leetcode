class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsMap = {}

        for n in nums:
            if n in numsMap:
                return True
            numsMap[n] = n
    
        return False