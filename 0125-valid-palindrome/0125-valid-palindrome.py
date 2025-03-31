class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = [x for x in ''.join(s.lower()) if x.isalnum()]
        n = len(t)
        for i in range(n//2):
            if t[i] != t[n - 1 - i]:
                return False
        return True