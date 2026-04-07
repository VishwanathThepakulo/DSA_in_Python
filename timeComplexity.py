import time

start_time = time.perf_counter()

# Access — O(1) time
num = [10,20,30,40,50,60,70,80,90,100]


# Access — O(1) time
print(num[5])
print(num[8])

end_time = time.perf_counter()


print(f"Total execution time: {end_time - start_time:.6f} seconds")




