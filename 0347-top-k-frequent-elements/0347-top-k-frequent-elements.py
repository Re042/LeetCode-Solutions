class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        answer = []
        for x in nums:
            freq[x] = 1 + freq.get(x, 0)
        while k > 0:    
            m = 0
            for x, y in freq.items():
                if y > m:
                    kl = x
                    m = y
            answer.append(kl)
            del freq[kl]
            k -= 1
        return answer
            
        