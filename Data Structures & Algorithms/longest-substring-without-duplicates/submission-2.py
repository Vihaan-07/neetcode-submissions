class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest = 1
        curr_sub = set()
        l,r = 0, 0
        while (l <= r) and (r < len(s)):
            ch = s[r]
            if ch in curr_sub:
                longest = max(longest, len(curr_sub))
                while True:
                    if s[l] == ch:
                        l+=1
                        break
                    curr_sub.remove(s[l])
                    l+=1
            # if ch is a new element
            curr_sub.add(ch)
            r+=1

        return max(longest, len(curr_sub))


            

        