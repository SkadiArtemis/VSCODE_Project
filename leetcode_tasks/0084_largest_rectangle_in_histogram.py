class Solution:
     def largestRectangleArea(self, heights):
        stack, idx = [], 0
        maxArea = 0
        while idx <= len(heights):
            curHeight = 0 if idx == len(heights) else heights[idx]
            if len(stack) == 0 or curHeight >= heights[stack[-1]]:
                stack.append(idx)
                idx += 1
            else:
                tmp = stack.pop()
                w = idx if len(stack) == 0 else (idx - stack[-1] - 1)
                maxArea = max(maxArea, heights[tmp] * w)
        
        return maxArea