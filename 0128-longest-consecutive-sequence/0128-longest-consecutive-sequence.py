class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        conseq = set(nums)
        m = 0
        for x in conseq:
            if x - 1 not in conseq:
                tmp = x
                k = 1
                while tmp + 1 in conseq:
                    tmp += 1
                    k += 1
                m = max(m, k)
        return m