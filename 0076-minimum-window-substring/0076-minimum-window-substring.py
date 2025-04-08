from collections import deque
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        leth = [0] * (ord('z') - ord('A') + 1)
        lets = set()
        for x in t:
            lets.add(x)
            leth[ord(x) - ord('A')] += 1
        tmp = [0] * (ord('z') - ord('A') + 1)
        deq = deque()
        l = len(s)
        ans = ''
        k = 0
        n = len(lets)
        for i in range(len(s)):
            if s[i] in lets:
                deq.append(i)
                tmp[ord(s[i]) - ord('A')] += 1
                if tmp[ord(s[i]) - ord('A')] == leth[ord(s[i]) - ord('A')]:
                    k += 1
                while k == n:
                    if i - deq[0] + 1 <= l:
                        ans = s[deq[0]:i+1]
                        l = i - deq[0] + 1
                    t = deq.popleft()
                    tmp[ord(s[t]) - ord('A')] -= 1
                    if tmp[ord(s[t]) - ord('A')] < leth[ord(s[t]) - ord('A')]:
                        k -= 1
        return ans


