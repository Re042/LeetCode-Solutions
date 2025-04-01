class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height)
        left = 0
        right = len(height) - 1
        mleft = height[left]
        mright = height[right]
        S = (right - left) * min(mleft, mright)
        while left < right:
            if height[left] < height[right]:
                while height[left] <= mleft:
                    left += 1
                    if left >= right:
                        return S
                mleft = height[left]
                S = max(S, (right - left) * min(mleft, mright))
            elif height[left] > height[right]:
                while height[right] <= mright:
                    right -= 1
                    if left >= right:
                        return S
                mright = height[right]
                S = max(S, (right - left) * min(mleft, mright))
            else:
                left += 1
                right -= 1
                if left >= right:
                    return S
                mleft = height[left]
                mright = height[right]
                S = max(S, (right - left) * min(mleft, mright))