class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key = lambda car: car[0], reverse = True)

        stack = []

        for car in cars:
            eta = (target-car[0]) / car[1]
            if stack and stack[-1] >= eta:
                continue # this car just joins the fleet
            stack.append(eta)

        return len(stack)
            
        