class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = -1
        for i in range(len(nums)):
            if nums[i] != val:
                left += 1
                nums[left] = nums[i]
        return left + 1