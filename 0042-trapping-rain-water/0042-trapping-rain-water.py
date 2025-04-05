class Solution:
    def trap(self, height: List[int]) -> int:
        S = 0
        lefts = [0]
        for i in range(1, len(height)):
            while height[i] > height[lefts[-1]]:
                k = lefts.pop()
                if not lefts:
                    break
                if height[i] >= height[lefts[0]]:
                    S += (k - lefts[-1]) * (height[lefts[0]] - height[k])
                else:
                    S += (k - lefts[-1]) * (height[i] - height[k])
            lefts.append(i)
        return S
                

