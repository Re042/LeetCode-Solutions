class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vfreq = {}
        freq = [[] for i in range ((len(nums) + 1))]
        answer = []
        for x in nums:
            vfreq[x] = 1 + vfreq.get(x, 0)
        for key, value in vfreq.items():
            freq[value].append(key)
        for i in range(len(freq) - 1, 0, -1):
            for x in freq[i]:
                answer.append(x)
                if len(answer) == k:
                    return answer
        