class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        cars = [(pos, sp) for pos, sp in zip(position, speed)]
        cars.sort(reverse = True)
        stack = (target - cars[0][0]) / cars[0][1]
        k = 1
        for i in range(1, n):
            t = (target - cars[i][0])/cars[i][1]
            if t > stack:
                stack = t
                k += 1
        return k
                
