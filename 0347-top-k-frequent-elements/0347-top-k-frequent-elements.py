class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        answer = []
        for x in nums:
            if x in freq.keys():
                freq[x] += 1
            else:
                freq[x] = 1
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
            
        