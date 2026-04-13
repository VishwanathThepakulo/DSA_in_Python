# Recursion means a function that calls itself is a recursive function

# Two Essential parts:
# Part                  Purpose
# Base Case             Stop the Recursion(Prevents Infinite loop)
# Recursive Case        calls itself with a smaller/simpler input

# without a base case --> RecursionError: maximum recursion depth exceeded

# def countdown(n):
#     if n == 0:
#         var = "Done!"
#         return var # Base Case   
#     print(n)
#     return countdown(n-1)
# print(countdown(5))




# Factorial


# def factorial(num):
#     if num == 0:
#         return 1 # Base Case   
#     return num*factorial(num-1)
# print(factorial(5))


# Fibonacci of n


# def fibonacci(num):
#     if num<=1:
#         return num
#     return fibonacci(num-1) + fibonacci(num-2)
# print(fibonacci(10))


# Sum of first n natural numbers

# def sum_of_natural(num):
#     if num<=1:
#         return num
#     return num+sum_of_natural(num-1)
# print(sum_of_natural(5))


# Power of a number (x^n)

def pow_of_num(x,y):
    if y==0:
        return 1
    return x*pow_of_num(x, y-1)
print(pow_of_num(2,3))







