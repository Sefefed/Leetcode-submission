class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq_cnt = defaultdict(int)
        freq = defaultdict(int)
        for num in tasks:
            freq[num] += 1
        max_ = 0
        for key in freq.values():
            if key > max_:
                max_ = key
            freq_cnt[key] += 1
        ans = max(len(tasks), (max_ - 1) * (n + 1) + freq_cnt[max_])
        return ans
        