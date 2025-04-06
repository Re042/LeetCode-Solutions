from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        let = [0] * 26
        for x in s1:
            let[ord(x) - ord('a')] += 1
        left = 0
        right = len(s1) - 1
        tmp = [0] * 26
        for i in range(left, right + 1):
            tmp[ord(s2[i]) - ord('a')] += 1
        if tmp == let:
            return True
        while right < len(s2) - 1:
            tmp[ord(s2[left]) - ord('a')] -= 1
            left += 1
            right += 1
            tmp[ord(s2[right]) - ord('a')] += 1
            if tmp == let:
                return True
        return False