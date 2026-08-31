class Solution(object):
    def topKFrequent(self, nums, k):
        buckets = [[] for _ in range(len(nums))]
        frequency = defaultdict(int)

        for n in nums:
            frequency[n] += 1

        for key, val in frequency.items():
            buckets[val-1].append(key)

        frequent = []

        for bucket in range(len(buckets)-1, -1, -1):
            if len(buckets[bucket]) == 0:
                continue
            for num in buckets[bucket]:
                frequent.append(num)
                if len(frequent) == k:
                    return frequent


        return frequent
        