class Solution:
    def productExceptSelf(self, nums):
        num_zeros = 0
        product = 1
        output = []
        for i, n in enumerate(nums):
            if n == 0 and num_zeros != 2:
                num_zeros += 1

            if n != 0:
                product = product * n

        if num_zeros >= 2:
            return [0 for _ in range(len(nums))]

        for n in nums:
            if n == 0:
                output.append(int(product))
            else:
                if num_zeros == 1:
                    output.append(0)
                    continue
                output.append(int(product/n))
        
        return output