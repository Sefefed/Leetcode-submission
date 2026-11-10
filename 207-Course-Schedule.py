class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for i in range(numCourses)]
        indegree = [0 for i in range(numCourses)]
        for ai, bi in prerequisites:
            graph[bi].append(ai)
            indegree[ai] += 1
        queue = deque()    
        order = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            cur = queue.popleft()
            order.append(cur)
            for ch in graph[cur]:
                indegree[ch] -= 1
                if indegree[ch] == 0:
                    queue.append(ch)
        return True if len(order) == numCourses else False             



