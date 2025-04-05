class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return piles[0] // h + 1 if piles[0] % h != 0 else piles[0] // h
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            t = 0
            for x in piles:
                t += x // mid + 1 if x % mid != 0 else x // mid 
            if t > h:
                left = mid + 1
            else:
                right = mid - 1
        return left
