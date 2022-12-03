class Solution:
    def dominantIndex(self, nums) -> int:
        large = max(nums)
        idx = nums.index(large)
        nums.remove(max(nums))
        secondlarge = max(nums)
        smallest = secondlarge * 2
        
        if large >= smallest:
            return idx
        else:
            return -1
                