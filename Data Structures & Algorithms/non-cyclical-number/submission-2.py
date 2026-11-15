class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}

        while True:
            sum = 0
            while n != 0:
                sum += (n%10) ** 2
                n //= 10
            n = sum

            if n == 1:
                return True
            if n in seen:
                return False
            
            seen.add(n)

            
            

        