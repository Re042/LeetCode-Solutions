class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mS = 0
        stack = []
        n = len(heights)
        for i in range(n + 1):
            while stack and (i == n or heights[i] <= heights[stack[-1]]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                S = height * width
                if S > mS:
                    mS = S
            stack.append(i)
        return mS