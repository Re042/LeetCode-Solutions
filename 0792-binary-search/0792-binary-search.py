class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        left = 0
        right = len(nums) - 1
        while right - left > 1:
            mid = (right + left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid
            else:
                return mid
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        return -1
