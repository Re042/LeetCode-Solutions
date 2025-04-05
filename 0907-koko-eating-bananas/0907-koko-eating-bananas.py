from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return ceil(piles[0] / h)
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            t = 0
            for x in piles:
                t += ceil(x/mid) 
            if t > h:
                left = mid + 1
            else:
                right = mid
        return left
