class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = {}
        for num in nums:
            freq_counter[num] = freq_counter.get(num, 0) + 1
        
        sorted_values = list(dict(sorted(freq_counter.items(), key=lambda item: item[1], reverse = True)).keys())

        return sorted_values[:k]