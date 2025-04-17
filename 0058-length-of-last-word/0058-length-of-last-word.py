class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        right = len(s) - 1
        while not s[right].isalpha():
            right -= 1
        k = 0
        while right >= 0 and s[right].isalpha():
            k += 1
            right -= 1
        return k
