class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # input output steps walkthrough
        # if one value appears more than once
        # nums = [1, 2 ,2 ,3 ,6]
        #  naive solution
            # for each number, first one , seen is empty, add first to seen ,
            # next, look in seen, if the subsequent nums are not seen, go next till done
            # if in seen, return Tue
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False

        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False


