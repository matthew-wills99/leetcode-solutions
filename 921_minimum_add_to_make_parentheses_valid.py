class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        invalidClose = 0
        waitingOpen = 0
        
        for i in range(len(s)):
            ch = s[i]
            if ch == '(':
                waitingOpen += 1
            else:
                if waitingOpen > 0:
                    waitingOpen -= 1
                else:
                    invalidClose += 1
                
                
        return waitingOpen + invalidClose