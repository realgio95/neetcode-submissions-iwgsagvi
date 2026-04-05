class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #  [1 2 3 4 5 6] , target = 5, t =2
        left = 0 
        right = len(nums) - 1 #5

        while left <= right:
            mid = (left + right)//2 # or left + (right - left) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left= mid+1
            else:
                right=mid-1

        return -1


