from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        let = defaultdict(int)
        for x in s1:
            let[x] += 1
        left = 0
        right = len(s1) - 1
        while right < len(s2):
            if s2[left] in let:
                tmp = let.copy()
                if tmp[s2[left]] != 1:
                    tmp[s2[left]] -= 1
                else:
                    del tmp[s2[left]]
                for i in range(left + 1, right+1):
                    if s2[i] not in tmp:
                        break
                    if tmp[s2[i]] != 1:
                        tmp[s2[i]] -= 1
                    else:
                        del tmp[s2[i]]
                if not tmp:
                    return True
            left += 1
            right += 1
        return False