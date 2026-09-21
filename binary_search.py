class Solution:
    def firstSearch(self, arr, k):
        low = 0
        high = len(arr)-1
        while low<=high:
            mid = low+(high//2)
            if arr[mid] == k:
                return arr[mid]
            elif arr[mid]<k:
                high = mid
            else:
                low = mid
        return -1
        
solution = Solution()
print(solution.firstSearch([1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,18,19,20,22,26,28,29,30],3))