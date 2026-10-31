class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for idx, height in enumerate(heights):
            start = idx

            while stack and stack[-1][1] > height:
                left, prev_height = stack.pop()
                area = prev_height * (idx - left)
                max_area = max(max_area, area)

                start = left  # Current height can extend this far left

            if not stack or stack[-1][1] < height:
                stack.append((start, height))

        n = len(heights)
        for left, height in stack:
            max_area = max(max_area, height * (n - left))

        return max_area