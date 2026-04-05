class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}

        for i, v in enumerate(nums):
            vals[v] = i

        for i, v in enumerate(nums):
            diff = target - v
            if (diff in vals and vals[diff]!=i):
                return [i, vals[diff]]
        return [-1, -1]
        