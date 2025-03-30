class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [[temperatures[0], 0]]
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                tmp = stack.pop()[1]
                answer[tmp] = i - tmp          
            stack.append([temperatures[i], i])
        return answer


