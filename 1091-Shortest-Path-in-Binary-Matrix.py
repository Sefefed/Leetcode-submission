class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[n - 1][m - 1]:
            return -1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        def inbound(row, col):
            if 0 <= row < n and 0 <= col < m:
                return True
            return False
        queue = deque([(0, 0, 1)])   
        visited = set()
        visited.add((0, 0))
        while queue:
            r, c, dist = queue.popleft()
            if r == n - 1 and c == m - 1:
                 return dist
            for dx, dy in directions:
                nr = r + dx
                nc = c + dy
                if inbound(nr, nc) and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1)) 
        return -1           
        