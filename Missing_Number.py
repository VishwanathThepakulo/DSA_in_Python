class Solution:
    def missingNumber(self, nums1: list[int]) -> int:
        nums = sorted(nums1)
        for i in range(len(nums)):
            if i==nums[i]:
                continue
            return i
        return len(nums)
    
nums = [0, 1]
sol = Solution()
print(sol.missingNumber(nums))