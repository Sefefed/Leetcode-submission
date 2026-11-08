class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Largest Rectangle in histogram so I need to follow certain rules
        # I have to consider the monotonic static problem 
        # so for each problem I hv to consider the previous smaller and the next smaller element for that matter I need to know the indexes to the both end so 
        # The area is gonna be r - l - 1 and the height is going to be current height
        # I need to have stack to store the indices
        stack = []
        heights.append(0)
        ans = 0
        n = len(heights)
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                l = stack[-1] if stack else -1
                w = i - l - 1
                ans = max(ans, height * w)
            stack.append(i)
        return ans    

               
        