class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) 
        k = r 
        while l <= r:
            m = (l+r) // 2
            t = self.time(piles, m)

            if t <= h:
                k = min(m, k)
                r = m-1
            else:
                l = m+1
        
        return k

    def time(self, arr, k):
        t=0
        for i in arr:
            t += math.ceil(i / k)
        
        return t
    
        