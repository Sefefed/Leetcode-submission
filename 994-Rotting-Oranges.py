class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        times = 0
        cnt = 0
        queue = deque([])
        def inbound(r, c):
            if 0 <= r < n and 0 <= c < m:
                return True
            return False    
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cnt += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))   
        while queue:
            k = len(queue)
            rotten = False
            for i in range(k):
                cr, cc = queue.popleft()
                for x, y in directions:
                    nr = cr + x
                    nc = cc + y
                    if inbound(nr, nc) and grid[nr][nc] == 1:
                        rotten = True
                        cnt -= 1
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
            if rotten:
                times += 1
        return times if cnt == 0 else -1    



        
        