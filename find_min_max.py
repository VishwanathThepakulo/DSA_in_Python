# class Solution:
#     def getMinMax(self, arr):
#         arr.sort()
#         return [arr[0],arr[len(arr)-1]] 

# solution = Solution()
# print(solution.getMinMax([1,2,3,4,5,0,7,8,9,10]))


class Solution:
    def getMinMax(self, arr):
        mini = arr[0]
        maxi = arr[0]
        for i in range(1,len(arr)):
            if mini > arr[i]:
                mini = arr[i]
            elif maxi < arr[i]:
                maxi = arr[i] 
        return [min, maxi]
        
        
arr = [28078, 19451, 935, 28892, 2242, 3570, 5480, 231]
solution = Solution()
print(solution.getMinMax(arr))
            