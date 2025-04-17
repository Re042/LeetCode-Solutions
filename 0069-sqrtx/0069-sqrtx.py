class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while left <= right:
            mid = (left + right) // 2
            tmp = mid ** 2
            if tmp == x:
                return mid
            elif tmp > x:
                right = mid - 1
            else:
                left = mid + 1
        return right