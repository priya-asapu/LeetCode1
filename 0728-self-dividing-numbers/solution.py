class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
         ans = []

         for num in range(left, right + 1):
            temp = num
            check = True

            while temp > 0:
                digit = temp % 10

                if digit == 0 or num % digit != 0:
                    check = False
                    break

                temp = temp // 10

            if check:
                ans.append(num)

         return ans
