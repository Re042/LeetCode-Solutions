class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = maxf if maxf > count[s[r]] else count[s[r]]
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = res if res > r - l + 1 else r - l + 1
        return res