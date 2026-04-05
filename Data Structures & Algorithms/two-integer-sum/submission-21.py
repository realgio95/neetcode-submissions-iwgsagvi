class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dict vals
        # [2, 3,4 5], target 7
        # start with 2, store in a dict, 2,0
        # at 3 look up the dict with 2 in it, t-3 see if 4 is there,
        # add 3
        # at 4, 
        # target
        # comp

        vals = {}
        for i,v in enumerate(nums):
            vals[v]=i
        for i, v in enumerate(nums):
            comp = target - v
            if (comp in vals and vals[comp] != i):
                return [i, vals[comp]]
            vals[v] = i
        return [-1,-1]            

        