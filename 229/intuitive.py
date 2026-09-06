from collections import defaultdict

class Solution:
    def majorityElement(self, nums):
        cnt = defaultdict(int)
        num_times = len(nums) // 3
        output = []

        if len(nums) == 2 and nums[0] != nums[1]:
            return nums
        elif len(nums) == 2 and nums[0] == nums[1]:
            return [nums[0]]

        for n in nums:
            cnt[n] += 1

        for n in cnt:
            if cnt[n] > num_times:
                output.append(n)

        return output
       