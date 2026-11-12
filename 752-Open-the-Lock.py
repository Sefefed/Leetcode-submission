class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        lock_dict = {"0": ["1", "9"], "1": ["0", "2"], "2": ["1", "3"], "3": ["2", "4"], "4": ["3", "5"], "5": ["4", "6"], "6": ["5", "7"], "7": ["6", "8"], "8": ["7", "9"], "9": ["8", "0"]}
        if target == "0000":
            return 0
        if "0000" in deadends:
            return -1    
        set_dead = set(deadends)
        visited = set()
        queue = deque(["0000"])
        visited.add("0000")
        move = 0
        while queue:
            n = len(queue)
            for j in range(n):
                cur_key = queue.popleft()
                for i in range(4):
                    one_p = cur_key[:i] + lock_dict[cur_key[i]][0] + cur_key[i+1:]
                    sec_p = cur_key[:i] + lock_dict[cur_key[i]][1] + cur_key[i+1:]
                    if one_p == target or sec_p == target:
                        return move + 1
                    if one_p not in visited and one_p not in set_dead:
                        queue.append(one_p)
                        visited.add(one_p)
                    if sec_p not in visited and sec_p not in set_dead:
                        queue.append(sec_p)
                        visited.add(sec_p)
            move += 1        
        return -1                    

            


        