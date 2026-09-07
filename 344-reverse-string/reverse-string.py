class Solution(object):
    def reverseString(self, s):
       st = 0
       l = len(s)-1
       m = len(s)//2
       while st<l :
            s[st],s[l]=s[l],s[st]
            l -= 1
            st += 1
       return s