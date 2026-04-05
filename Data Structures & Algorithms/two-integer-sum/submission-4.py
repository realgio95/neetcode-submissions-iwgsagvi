class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #  2 3 4 5 , t = 7
        #  regular manner 
        #    start at 2, look at 3,  check if sum is 7

        #    for i = 0 to N:
        #         for j = i + 1 to N
        #             sumij = nums[i] + num j
        #             if sumij == target
        #                 return (i, j)

        # start at 2, add two to a dictCheck {2:0, 3:1}, check if complementOf2 (5) in current dict
        #     if complement of 2 in the dict
        #         return pair
        #     add 2,0 to dict   
        dictC = {}
        for i in range(0,len(nums)):
            comp = target - nums[i]
            if (comp in dictC):
                return [dictC[comp], i]
            else:
                dictC[nums[i]] = i     

        return [-1, -1]
        
        #  as N grows, dictC grows with it linearly
        # as N grows, the time complexity grows with it linearly