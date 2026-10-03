from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht = defaultdict(int)
        for num in nums:
            ht[num] += 1
        return list(sorted(ht, key=lambda num: ht[num], reverse=True))[:k]