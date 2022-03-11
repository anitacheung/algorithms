class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        i = 0
        max = 0
        for char in s:
            j = i + 1
            sub = s[i]
            while j < len(s):
                if s[j] in sub:
                    print(sub)
                    break
                else:
                    sub += s[j]
                    j += 1
            if max < j - i:
                max = j - i
            i += 1
        
        return max
    
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        faster to use a map
        """
        
        i = 0
        max = 0
        for char in s:
            j = i + 1
            sub = {s[i]:1}
            while j < len(s):
                if s[j] in sub:
                    break
                else:
                    sub[s[j]] = 1
                    j += 1
            if max < j - i:
                max = j - i
            i += 1
        
        return max