class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # in 2 3 4 5 , 7
        # out : [[2,5], [3,4]]
        # cases to think about, when all used up, when choice beyond the target value, and when target reached 
        def dfs(i, curr, t):
            if i >= len(nums):
                return

            if t == 0:
                res.append(curr.copy())
                return
        
            if t < 0:
                return

            curr.append(nums[i])
            dfs(i, curr, t-nums[i])
            curr.pop()
            dfs(i+1, curr, t)

        dfs(0, [], target)
        return res