class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ls = s.split()
        count = 0
        for c in ls[len(ls) - 1]:
            count += 1
        
        return count