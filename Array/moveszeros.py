
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.


class Solution: 
    def moveZeroes(self, nums):
        i = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[i], nums[r] = nums[r], nums[i]
                i += 1


# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]