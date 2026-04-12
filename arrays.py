# Array is a data structure which stores same type of values in continuous memory
# Why :- Fast Access, memory efficient, base of all DSA(Stack, queue, hashmap)

# Create
nums = [1,2,3,4,5,6,7,8,9,10]

# # Access -O(1)
# print(nums[0])
# print(nums[-1])
# print(nums[1:3])

# # Update  -O(1)
# nums[2]=100
# print(nums)

# Append and insert
# Append at the end  -O(1) Fast
# nums.append(100)
# print(nums)

# Append at the middle -O(n) slow

# nums.insert(2,100)
# print(nums)


# pop() last — O(1) Fast 

# nums.pop()
# print(nums)


# pop(index) middle — O(n) Slow

# print(nums.pop(1))
# print(nums)
# nums.remove(1)
# print(nums)


# search

# nums = [1,2,3,4,5,6,7,8,9,10]

# # Linear search -O(n)

# def linear_search(nums, target):
#     for i in range(len(nums)):
#         if nums[i]==target:
#             return i
#     return -1

# print(linear_search(nums, 10))
# print(linear_search(nums, 11))


# # 1. Find max
# nums = [1,2,3,4,5,6,7,8,9,10]

# def find_max(nums):
#     max_val = nums[0]
#     for num in nums:
#         if max_val<num:
#             max_val=num
#     return max_val

# print(find_max(nums))
    
# revere an array
# nums = [1,2,3,4,5,6,7,8,9,10]

# def rev_arr(nums):    
#     return nums[::-1]
# print(rev_arr(nums))


# Check Duplicatezs
# nums = [1,2,3,4,5,6,7,8,9,10,1,2]
# def has_duplicates(nums):
#     return len(nums) != len(set(nums))
# print(has_duplicates(nums))


# 4. Sum of Array

# nums = [1,2,3,4,5,6,7,8,9,10,1,2]

# def sum_of_array(nums):
#     return sum(nums)

# print(sum_of_array(nums))

# Second largest array
# nums = [1,2,3,4,5,6,7,8,9,10,1,2]

# def second_largest(nums):
#     nums.sort()
#     return nums[-2]
# print(second_largest(nums))






# Remove duplicates


arr = [1,1,2,3,4,5,2,1,4,100]
class Solution:
    def remDuplicate(self, arr):
        # code here 
        return list(set(arr))
    
solution = Solution()
print(solution.remDuplicate(arr))
























