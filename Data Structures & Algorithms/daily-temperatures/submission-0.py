class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]* len(temperatures)
        stack = []
        for idx, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                top = stack[-1]
                result[top[1]] = idx - top[1]
                stack.pop()
                
            stack.append((val, idx))
        
        return result
            
            


            



        