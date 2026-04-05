class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        # 1 2 3 4 5 , t 5
        for i, v in enumerate(nums):
            diff = target - nums[i]
            if (diff in prevMap):
                return [prevMap[diff],i] 
            prevMap[v] = i
        return [-1, -1]