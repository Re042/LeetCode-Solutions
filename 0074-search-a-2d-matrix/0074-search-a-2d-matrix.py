class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[0][0] > target:
            return False
        up = 0
        down = len(matrix) - 1
        while up <= down:
            mid = (up + down) // 2
            if matrix[mid][0] < target:
                up = mid + 1
            elif matrix[mid][0] > target:
                down = mid - 1
            else:
                return True
        left = 0
        right = len(matrix[down]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[down][mid] < target:
                left = mid + 1
            elif matrix[down][mid] > target:
                right = mid - 1
            else:
                return True
        return False