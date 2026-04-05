class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # input output steps walkthrough
        # if one value appears more than once
        # nums = [1, 2 ,2 ,3 ,6]
        #  naive solution see for each number, first one is empty, add to seen , next, look in seen
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False
