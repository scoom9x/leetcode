class Solution:
    def majorityElement(self, nums):
        candidate1 = candidate2 = None
        count1 = count2 = 0

        # Find 2 possible candidates
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 = 1
            elif count2 == 0:
                candidate2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Verify the candidates
        output = []

        for candidate in (candidate1, candidate2):
            if nums.count(candidate) > len(nums) // 3:
                output.append(candidate)

        return output