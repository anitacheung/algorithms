class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        binary = str(bin(n))
        total = 0
        for char in binary:
            if char=="1":
                total += 1
        return total
        