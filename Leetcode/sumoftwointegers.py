class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        result = 0
        if (a==0):
            return b
        elif (b==0):
            return a
        elif (a < 0 and b < 0):
            for i in range(-a):
                result -= 1
            for i in range(-b):
                result -= 1
        elif (a < 0 or b < 0):
            result = a % b
        elif (a > 0 and b > 0):
            for i in range(a):
                result += 1
            for i in range(b):
                result += 1
        return result