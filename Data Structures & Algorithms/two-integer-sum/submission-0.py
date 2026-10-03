class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for index, num in enumerate(nums):
            if target - num in ht:
                return [ht[target - num], index]
            else:
                ht[num] = index