class Solution:
    def lengthOfLongestSubstring(self, a: str) -> int:
        lis = []
        j = 0 
        for j in range(len(a)):
            ch = ''
            for i in range(j, len(a)):
                if a[i] in ch:
                    break
                ch += a[i]
            lis.append(ch)
            j+=1
        longest = max(lis, key=len)
        return len(longest)
s = "pwwkew"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))














