
# Big O Complexity Chart

# O(1)        → Best  🟢  — Constant
# O(log n)    → Good  🟢  — Binary Search
# O(n)        → OK    🟡  — Linear Search
# O(n log n)  → OK    🟡  — Merge Sort
# O(n²)       → Bad   🔴  — Nested Loops
# O(2ⁿ)       → Worst 🔴  — Recursion without memoization





import time

# start_time = time.perf_counter()
# # Access — O(1) time
# nums = [10,20,30,40,50,60,70,80,90,100]

# # Access — O(1) time---------1
# # O(1) — Constant Time (Direct Access)
# print(nums[5])
# # print(nums[8])

# end_time = time.perf_counter()
# print(f"Total execution time----------1: {end_time - start_time:.6f} seconds")

# # start_time = time.perf_counter()

# # end_time = time.perf_counter()
# # print(f"Total execution time: {end_time - start_time:.6f} seconds")


# start_time = time.perf_counter()

# print(nums.pop(1))

# end_time = time.perf_counter()
# print(f"Total execution time: {end_time - start_time:.6f} seconds")



# start_time = time.perf_counter()

# def find_element(arr, target):
#     for item in arr:
#         if item == target:
#             return True
#     return False
# print(find_element(nums, 33))
# end_time = time.perf_counter()
# print(f"Total execution time: {end_time - start_time:.6f} seconds")

# start_time = time.perf_counter()
# big_nums = list(range(10000000))
# x= big_nums[500]
# end_time = time.perf_counter()
# print(f"O(1) Access: {end_time-start_time:.8f}")

# print('------------------------------------------')

# start_time = time.perf_counter()
# for i in big_nums:
#     if i == 9999999:
#         break
# end_time =  time.perf_counter()
# print(f"O(n) Access: {end_time-start_time:.8f}")


# start_time = time.perf_counter()
# big_nums.pop()
# end_time =  time.perf_counter()
# print(f"O(1) Access: {end_time-start_time:.8f}")


# print('------------------------------------------')

# start_time = time.perf_counter()
# big_nums.pop(0)
# end_time =  time.perf_counter()
# print(f"O(n) Access: {end_time-start_time:.8f}")



#  O(n^2) — Quadratic Example (Bubble Sort)
# A classic "bad" complexity. To sort a list using Bubble Sort, you compare every item to its neighbor in nested loops.
# Why it's O(n^2): If you have 2,000 items, the computer does roughly 2,000 times 2,000 = 4,000,000 comparisons. If you double the list to 4,000 items, the time will quadruple.



# arr = list(range(2000,0,-1))
# arr = list(range(1,11))
# print(arr)

# def bubble_sort(arr):
#     n = len(arr)
#     SWAP = False
#     for i in range(n):
#         for j in range(n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#                 SWAP = True
#             if not SWAP:
#                 break   
#     return arr

# start = time.perf_counter()
# print(bubble_sort(arr))
# end = time.perf_counter()

# print(f"O(n^2) time taken is : {end-start:.6f}")




# O(log n) — Logarithmic Example (Binary Search)
# This is the "gold standard" for searching. It is incredibly fast because it throws away half of the data with every step.

# Why it's O(\log n): Even with 1,000,000 items, Binary Search only needs about 20 steps to find the answer. It is so fast that time.perf_counter() might show 0.0000 seconds on a modern machine.



# arr = list(range(1000000))

# def binary_search(arr, target):
#     low = 1
#     high = len(arr)-1
#     while low<=high:
#         mid = (low+high)//2
#         if arr[mid]==target:
#             return mid
#         elif arr[mid]<target:
#             low=mid+1
#         else:
#             high = mid-1
#     return -1
# start = time.perf_counter()

# print(binary_search(arr,9999))

# end = time.perf_counter()
# print(f"O(log n) Binary Search took: {end - start:.8f} seconds")











import time



def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 1. Divide: Find the midpoint and split the list (log n steps)
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 2. Conquer: Merge the sorted halves (n steps)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # Compare elements from both halves and build the sorted list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    # Add any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Testing with 10,000 items
# (Try this against the Bubble Sort from before—the difference is massive!)
data = list(range(10,0,-1))

start = time.perf_counter()
sorted_data = merge_sort(data)
end = time.perf_counter()

print(f"O(n log n) Merge Sort took: {end - start:.4f} seconds")









































































































