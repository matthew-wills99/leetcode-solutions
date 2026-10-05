"""
keep checking until we find a set of parentheses that terminates immediately '()'
replace that set with 1
"""

class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        score = 0
        d = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                d += 1
            else:
                d -= 1
                if s[i - 1] == '(':
                    score += 2 ** d
        return score