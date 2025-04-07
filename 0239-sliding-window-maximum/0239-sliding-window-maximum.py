class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        deq = [0]
        ans.append(max(nums[0:k]))
        for i in range(1, len(nums)):
            if i - deq[0] == k:
                deq.pop(0)
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
            deq.append(i)
            if i >= k:
                ans.append(nums[deq[0]])
        return ans