class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in range(len(s)):
            val = 26 - ord(s[i]) + ord('a')
            ans += val * (i + 1)
        return ans    
