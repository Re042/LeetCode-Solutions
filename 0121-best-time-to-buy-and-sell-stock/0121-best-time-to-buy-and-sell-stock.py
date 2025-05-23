class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        mprof = 0
        while right < len(prices):
            if prices[left] >= prices[right]:
                left = right
            else:
                prof = prices[right] - prices[left]
                if prof > mprof:
                    mprof = prices[right] - prices[left]
            right += 1
        return mprof
