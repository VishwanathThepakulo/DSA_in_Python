
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
big_nums = list(range(10000000))
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


start_time = time.perf_counter()
big_nums.pop()
end_time =  time.perf_counter()
print(f"O(1) Access: {end_time-start_time:.8f}")


print('------------------------------------------')

start_time = time.perf_counter()
big_nums.pop(0)
end_time =  time.perf_counter()
print(f"O(n) Access: {end_time-start_time:.8f}")