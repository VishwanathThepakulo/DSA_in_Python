# class Solution:
#     def search(self, arr, x):
#         # code here
#         for i in range(len(arr)):
#             if arr[i]==x:
#                 return i
#         return -1
    
# solution = Solution()
# print(solution.search([1,5,9,2],9))


class Solution:
    def search(self, arr, x):
        # code here
        for i,j in enumerate(arr):
            if arr[i]==x:
                return i
        return -1
    
solution = Solution()
print(solution.search([1,5,9,2],9))