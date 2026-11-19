class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #  [ 1 2 3 4 5], t = 6
        # 1 diff = 5. look it up in a hashmap prev, add to prev if not diff not found

        comp = {}

        for i, v in enumerate(nums):
            diff = target - v
            if diff in comp:
                return [comp[diff], i]
            comp[v] = i

        return [-1,-1]
        



