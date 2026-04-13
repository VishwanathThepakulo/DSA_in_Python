# Recursion means a function that calls itself is a recursive function

# Two Essential parts:
# Part                  Purpose
# Base Case             Stop the Recursion(Prevents Infinite loop)
# Recursive Case        calls itself with a smaller/simpler input

# without a base case --> RecursionError: maximum recursion depth exceeded

# def countdown(n):
#     if n == 0:
#         var = "Done!"
#         return var
#     print(n)
#     return countdown(n-1)
# print(countdown(5))




# Factorial


def factorial(num):
    if num == 0:
        return 1
    return num*factorial(num-1)
print(factorial(5))