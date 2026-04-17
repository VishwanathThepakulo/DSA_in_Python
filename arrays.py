# Array is a data structure which stores same type of values in continuous memory
# Why :- Fast Access, memory efficient, base of all DSA(Stack, queue, hashmap)

# Create
# nums = [1,2,3,4,5,6,7,8,9,10]

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


# arr = [1,1,2,3,4,5,2,1,4,100]
# class Solution:
#     def remDuplicate(self, arr):
#         # code here 
#         return list(set(arr))
    
# solution = Solution()
# print(solution.remDuplicate(arr))

# Reverse list without built-in
# arr = [1,1,2,3,4,5,2,1,4,100,100]  #Two pointers
# left = 0
# right = len(arr)-1
# while left<right:
#     arr[left], arr[right]=arr[right],arr[left]
#     left+=1
#     right-=1
# print(arr)
    





# Find second largest number ---set = O(n) sort = O(n log n)
# arr = [1,1,2,3,4,5,2,1,4,80,100,100,80,90,90,1]
# arr1 = list(set(arr))
# print(arr1)
# arr1.sort()
# print(arr1[-2])

# arr = [1,1,2,80,100,100,90]
# first = second = float('-inf')
# for num in arr:
#     if num > first:
#         second = first
#         first = num
#     elif num>second and num!=first:
#         second = num
# print(second)
        



# arr = [1,1,2,3,4,5,2,1,4,80,100]
# for i in arr:
#     print(i)



# Remove duplicates
# arr = [1,1,2,3,4,5,2,1,4,80,100]
# def remDuplicate(arr):
#     emp_lis=[]
#     for i in arr:
#         if i not in emp_lis:
#             emp_lis.append(i)
#     return emp_lis

# print(remDuplicate(arr))
            

# Find sum of even numbers
# arr = [1,2,3,4,5,6,7,8,9,10]
# def sum_of_even(arr):
#     n = 0
#     for i in arr:
#         if i%2==0:
#             n+=i
#     return n
# print(sum_of_even(arr))  



# Check palindrome list
# arr = [1,2,3,2,1]

# def palindrome_list(arr):
#     if arr == arr[::-1]:
#         return "Palindrome"
#     return "Not a Palindrome"
    
# print(palindrome_list(arr))




# 1️⃣ Move all zeros to end
# 👉 [0,1,0,3,12] → [1,3,12,0,0]
arr = [0,1,0,3,12]
for i in arr:
    if i == 0:
        arr.pop(i)
        arr.append(0)
print(arr)








# 2️⃣ Find missing number (1 to n)

# 3️⃣ Rotate array (right/left)

# 4️⃣ Find duplicate element (without set)

# 5️⃣ Two sum (important interview question)


# Now try these without built-ins:

# 1️⃣ Move zeros to end
# 2️⃣ Rotate array
# 3️⃣ Two sum
# 4️⃣ Find missing number
# 5️⃣ Find duplicate (no set)

