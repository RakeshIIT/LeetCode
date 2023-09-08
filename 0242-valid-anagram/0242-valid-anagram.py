class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(s,t)
        s=list(s)
        s.sort()
        t=list(t)
        t.sort()
        print(s,t)
        if s==t:
            return True
        else:
            return False