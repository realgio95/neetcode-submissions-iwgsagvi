class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i, v in enumerate(nums):
            diff = target - v
            if (diff in vals):
                return [vals[diff], i]
            vals[v] = i
        