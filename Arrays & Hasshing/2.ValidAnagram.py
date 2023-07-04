class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1= list(s)
        t1= list(t) 
        z= t1+s1
        h = 0
        z.sort
        for lista in range(0,len(z)-2):
           if z[lista] == z[lista+1]:
               h += 1
        
        if h == len(s1):
            return True
        
        return False