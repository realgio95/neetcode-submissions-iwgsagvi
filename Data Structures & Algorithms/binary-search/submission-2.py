class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # array sorted 1 2 3 4 5, t 2
        length = len(nums)
        start = 0
        end = length - 1

        while start <= end:
            mid = start + (end - start) // 2    
            if (nums[mid] == target):
                return mid
            elif (target < nums[mid]):
                end = mid - 1
            else:
                start = mid+1
        
        return -1

                
    
        