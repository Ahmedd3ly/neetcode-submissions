class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)

        stack = []

        for pos, spd in sorted(cars)[::-1]:
            eta = (target - pos) / spd

            if not stack or eta > stack[-1]:
                stack.append(eta)

        return len(stack) 