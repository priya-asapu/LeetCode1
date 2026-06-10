class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        new=set()
        for i in arr:
            if i*2 in new or i/2 in new:
                return True
            new.add(i)
        return False
