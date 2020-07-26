class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def binHelper(low, high):
            if low >= high:
                return nums[high]
            if nums[low] == nums[high] and low != high:
                return binHelper(low + 1, high)
            mid = int((high + low) / 2)
            if nums[mid] > nums[high]:
                return binHelper(mid + 1, high)
            else:
                return binHelper(low, mid)
        
        return binHelper(0, len(nums) - 1)
