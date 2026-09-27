class Solution:
    def maxPrefixSumQueries(self, arr, queries):
        ans = []
        for L, R in queries:
            running = 0
            best = float("-inf")
            for i in range(L, R+1):
                running = running+arr[i]
                if running>best:
                    best = running
            ans.append(best)
        return ans
    
arr = [-1, 2, 3, -5]
queries = [[0, 3], [1, 3]]
solution = Solution()
print(solution.maxPrefixSumQueries(arr, queries))





