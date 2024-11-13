# 26. Remove duplicates from sorted array
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left, right, k = 0,1,1
        while right < len(nums):
            if nums[left]!= nums[right]:
                nums[k] = nums[right]
                left = right
                k += 1
            right += 1
        return k
