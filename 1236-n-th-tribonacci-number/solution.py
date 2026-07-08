class Solution:
    def tribonacci(self, n: int) -> int:
        f1 = 0
        f2 = 1
        f3 = 1

        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        for i in range(3, n + 1):
            f = f1 + f2 + f3
            f1 = f2
            f2 = f3
            f3 = f

        return f3
