# Linear Search

import time


arr = [1,2,3,4,5,6,7,8,9,10]

def linear_search(arr, target):
    length = len(arr)
    for i in range(length):
        if target == arr[i]:
            return i
    return -1

# start = time.perf_counter()
# print(linear_search(arr,10))
# end = time.perf_counter()
# print(f"Time complexity for Linear Search {end - start:.6f}") #O(n)


print("======================================")
# Binary Search


# arr = [1,2,3,4,5,6,7,8,9,10]
# print(len(arr))
# left = 0
# right = len(arr)-1
# print( f"mid = {left+right//2}")

def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif mid < target:
            left = mid+1
        else:
            right = mid-1
    return -1
start = time.perf_counter()
print(binary_search(arr, 10))
end = time.perf_counter()
print(f"Time complexity for Linear Search {end - start:.6f}")


















