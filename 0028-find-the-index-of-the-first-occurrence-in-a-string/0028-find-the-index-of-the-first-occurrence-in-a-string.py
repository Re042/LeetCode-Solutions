class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        let = needle[0]
        l = 0
        r = 0
        while l <= len(haystack) - len(needle):
            while r <= len(needle) - 1 and haystack[l+r] == needle[r]:
                r += 1
            if r == len(needle):
                return l
            l += 1
            r = 0
        return -1