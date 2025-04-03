class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        let = {}
        msub = 0
        left = 0
        right = 0
        while right < len(s):
            if s[right] in let and let[s[right]] >= left:
                sub = right - left
                if sub > msub:
                    msub = sub
                left = let[s[right]] + 1
            let[s[right]] = right
            right += 1
        sub = right - left
        return sub if sub > msub else msub