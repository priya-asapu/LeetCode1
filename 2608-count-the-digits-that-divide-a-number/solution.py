class Solution:
    def countDigits(self, num: int) -> int:
       count=0
       n1=num
       while n1>0:
        i=n1%10
        if i!=0 and num%i==0:
         count+=1
        n1=n1//10
       return count 
