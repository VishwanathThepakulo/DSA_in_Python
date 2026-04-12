# Linear Search

arr = [1,2,3,4,5,6,7,8,9,10]

def linear_search(arr, target):
    length = len(arr)
    for i in range(length):
        if target == arr[i]:
            return i
    return -1

print(linear_search(arr,10))























