class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
            two strings 
            s and t
            check if all of them have same number of chars
        '''
        if len(s) != len(t):
            return False
            
        s_d = {}
        t_d = {}
        for x in s:
            if x in s_d:
                s_d[x] += 1
            else:
                s_d[x] = 1
        for y in t:
            if y in t_d:
                t_d[y] += 1
            else:
                t_d[y] = 1
        print(s_d)
        print(t_d)
        for k,v in s_d.items():
            if k not in t_d or t_d[k] != v:
                return False
        return True
                
            

