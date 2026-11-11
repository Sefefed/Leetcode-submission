class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        cnt = 0
        max_ = max(arr2)
        for num in arr1:
            is_True = True
            for num1 in arr2:
                if abs(num - num1) <= d:
                    is_True = False
                    break
            if is_True:
                cnt += 1
        return cnt                
        