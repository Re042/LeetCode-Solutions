class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = {}
        for i in range(len(nums)):
            if target - nums[i] in sol.keys():
                return [i, sol[target - nums[i]]]
            sol[nums[i]] = i
