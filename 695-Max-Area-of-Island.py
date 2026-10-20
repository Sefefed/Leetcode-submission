class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for i in range(n)]
        ans = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def bfs(r, c):
            queue = deque([(r, c)])
            cur = 1
            visited[r][c] = True
            while queue:
                r, c = queue.popleft()          
                for dx, dy in directions:
                    nr, nc = r + dx, c + dy
                    if nr >= 0 and nc >= 0 and nr < n and nc < m and grid[nr][nc] == 1 and not visited[nr][nc]:
                        cur += 1
                        visited[nr][nc] = True
                        queue.append((nr, nc))
            return cur
        for r in range(n):
            for c in range(m):
                if not visited[r][c] and grid[r][c] == 1:
                    ans = max(ans, bfs(r, c))
        return ans            





        
                    
            
        