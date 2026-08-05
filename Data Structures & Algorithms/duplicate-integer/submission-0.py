class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)

        # if the set and the list have the same num of elements, there is 0 duplicates
        if len(nums_set) == len(nums):
            return False
        else:
            return True
        