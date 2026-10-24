class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest_seq = 0
        for i in nums:
            # we check if i is the beginning of a sequence
            if i-1 not in hashset:
                length = 0
                while i+length in hashset:
                    length += 1
                longest_seq = max(length, longest_seq)

        return longest_seq


    

        