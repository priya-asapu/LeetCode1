class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        total = 0

        for num in set(nums):
            if nums.count(num) == 1:
                total += num

        return total

            
            
