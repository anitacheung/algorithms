class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        output = []
        for i in range(n + 1):
            val = str(bin(i))
            total = 0
            for char in val:
                if (char == "1"):
                    total += 1
            output.append(total)
        
        return output