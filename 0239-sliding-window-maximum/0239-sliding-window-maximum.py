from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        deq = deque()
        deq.append(0)
        if k == 1:
            ans.append(nums[deq[0]])
        for i in range(1, len(nums)):
            if i - deq[0] == k:
                deq.popleft()
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
            deq.append(i)
            if i >= k - 1:
                ans.append(nums[deq[0]])
        return ans