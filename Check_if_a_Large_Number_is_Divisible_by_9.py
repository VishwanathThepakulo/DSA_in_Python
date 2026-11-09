class Solution:
    def isDivisibleBy9(self, s: str) -> bool:
        # Your code goes here
        no = int(s)
        sum = 0
        while no > 0:
            rem = no%10
            sum=sum+rem
            no=no//10
        print(sum)
        if sum%9==0:
            return True
        return False
    
solution = Solution()
print(solution.isDivisibleBy9("234567876799333"))
            
            
# no = 12345
# sum = 0
# while no>0:
#     rem = no%10
#     sum = sum+rem
#     no=no//10
# print(sum)