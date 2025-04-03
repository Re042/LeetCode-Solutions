class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif ((nums[mid] > target >= nums[left]) 
            or (nums[mid] < nums[left] <= target) 
            or (nums[left] > nums[mid] > target)):
                right = mid -1
            else:
                left = mid + 1
        return -1