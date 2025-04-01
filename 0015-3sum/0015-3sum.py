class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        ans = []
        for i in range(2, len(nums)):
            if i != len(nums) - 1 and nums[i+1] == nums[i]:
                continue
            left = 0
            right = i - 1
            while left < right:
                tmp = nums[left] + nums[right] + nums[i]
                if tmp < 0:
                    left += 1
                elif tmp > 0:
                    right -= 1
                else:
                    ans.append([nums[left], nums[right], nums[i]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    right -= 1
        return ans