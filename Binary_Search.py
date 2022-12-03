class Solution:
    def search(self, nums, target) -> int:
        left = 0
        right = len(nums)-1
    
        while left <= right: 
            mid = right - left
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1