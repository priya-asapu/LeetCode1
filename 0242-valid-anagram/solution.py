class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=list(s)
        l1=list(t)
        l.sort()
        l1.sort()
        a="".join(l)
        b="".join(l1)
        if a==b:
           return True
        else:
            return False

