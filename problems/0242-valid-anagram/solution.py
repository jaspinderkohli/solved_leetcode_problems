class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        check_s = {}
        for i in s:
            if i not in check_s.keys():
                check_s[i] = 1
            else:
                check_s[i] += 1
        print(check_s)
        
        check_t = {}
        for i in t:
            if i not in check_t.keys():
                check_t[i] = 1
            else:
                check_t[i] += 1
        print(check_t)
        for k in check_s.keys():
            if check_s[k] != check_t.get(k, 0):
                return False
        return True
