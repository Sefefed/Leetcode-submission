class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        set_ = set()
        n = len(s)
        for i in range(n):
            if s[i] == 'a' and 'b' in set_:
                return False
            set_.add(s[i])
        return True        

        