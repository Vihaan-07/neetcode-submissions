class Solution:
    def isPalindrome(self, s: str) -> bool:
        w = "".join(s.split())
        w = w.lower()
        w = re.sub(r'[^a-z0-9]', '', w)
        i = 0
        j = len(w)-1
        while i < j:
            if w[i] != w[j]:
                return False
            i+=1
            j-=1
        return True