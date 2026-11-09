class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        def inbound(r, c):
            if 0 <= r < n and 0 <= c < m:
                return True
            return False   
        queue = deque([]) 
        islands = 0    
        def bfs(r, c):
            queue.append((r, c))
            while queue:
                cr, cc = queue.popleft()
                for x, y in directions:
                    nr, nc = cr + x, cc + y
                    if inbound(nr, nc) and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        queue.append((nr, nc))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    islands += 1
                    bfs(i, j)
        return islands                             
                        





        