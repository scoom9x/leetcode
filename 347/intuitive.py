from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        most_frequent = []

        for n in nums:
            frequency[n] += 1
        
        for n in range(k):
            y, greatest = 0, 0

            for key, value in frequency.items():
                if value > greatest:
                    greatest = value
                    y = key

            most_frequent.append(y)
            frequency.pop(y)
        
        return most_frequent