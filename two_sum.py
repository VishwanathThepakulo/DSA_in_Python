# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(1,len(nums)):
#                 if i==j:
#                     continue
#                 if nums[i]+nums[j]==target:
#                     return [i,j]
     
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i   
        
        
# class Solution:
#     def twoSum(self, nums, target):
#         left = 0
#         right = len(nums)-1       
#         while left<right:
#             total = nums[left]+nums[right]
#             if total == target:
#                 return [left, right]
#             elif total<target:
#                 left+=1                
#             else:
#                 right-=1
        
        
nums =  [3,2,4]
target = 6
sol = Solution()
print(sol.twoSum(nums, target))
        
        
        
        
        
        
        
        
        
        