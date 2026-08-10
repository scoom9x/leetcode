from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsCount = defaultdict(int)

        for n in nums:
            numsCount[n] += 1

        highestVal = 0
        highestCnt = 0
        for n in numsCount:

            if numsCount[n] > highestVal:
                highestVal = numsCount[n]
                highestCnt = n
        return highestCnt
