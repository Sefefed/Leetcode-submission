class Solution(object):
    def taskSchedulerII(self, tasks, space):
        """
        :type tasks: List[int]
        :type space: int
        :rtype: int
        """

        last_day = defaultdict(int)
        cur_day = 0
        for task in tasks:
            cur_day += 1
            if task in last_day:
                if cur_day - last_day[task] <= space:
                    cur_day += space + 1 - (cur_day - last_day[task])
            last_day[task] = cur_day
        return cur_day  




        