class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # inputs nums , output bool steps - go through each nums. if curr in dict return true,
        #  analysis 2 3 4 3 t3, [3] {2,3}, O(N), O(N)
        #  could be logn if sorted, keep doing binary search, look to the right
        dup_dict = set()
        
        for curr in nums:
            if curr in dup_dict:
                return True 
            else:
                dup_dict.add(curr)
        return False
         