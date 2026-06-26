class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        maxArea = 0

        for i, h in enumerate(heights):
            startInd = i
            while stack and h < stack[-1][1]:
                poppedInd, poppedHeight = stack.pop()

                width = i - poppedInd
                maxArea = max(maxArea, poppedHeight * width)
                startInd = poppedInd
            stack.append([startInd, h])

        for i, h in stack:
            width = len(heights) - i
            maxArea = max(maxArea, h * width)

        return maxArea