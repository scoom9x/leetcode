class Solution:
    def swap(self, nums, k, j):
        nums[k], nums[j] = nums[j], nums[k]

    def shiftDown(self, nums, i, upper):
        while True:
            l, r = i * 2 + 1, i * 2 + 2
            if r < upper:
                if nums[i] >= max(nums[l], nums[r]):
                    break
                elif nums[l] > nums[r]:
                    self.swap(nums, i, l)
                    i = l
                else:
                    self.swap(nums, i, r)
                    i = r
            elif l < upper:
                if nums[i] >= nums[l]:
                    break
                else:
                    self.swap(nums, i , l)
                    break
            else:
                break
                
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range((len(nums) - 2) // 2, -1, -1):
            self.shiftDown(nums, i, len(nums))

        for end in range(len(nums) - 1, 0, -1):
            self.swap(nums, 0, end)
            self.shiftDown(nums, 0, end)
        return nums