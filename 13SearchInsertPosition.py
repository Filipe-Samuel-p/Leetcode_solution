class Solution(object):
    def searchInsert(self, nums, target):
        
        if target in nums:
            for index in range(len(nums)):
                if nums[index] == target:
                    return index
        else:
            for index in range(len(nums)):
                if nums[index] > target:
                    return (index)
                if index == len(nums) - 1:
                    return index +