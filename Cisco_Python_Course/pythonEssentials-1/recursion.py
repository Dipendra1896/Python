# recursion is a technique where a function invokes itself. fibonacci is an example of recursion

#A function can call other functions, or even itself. When a function calls itself, this situation is known as recursion, and the function which calls itself and contains a specified termination condition (i.e., the base case − a condition which doesn't tell the function to make any further calls to that function) is called a recursive function.
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)

for n in range(1, 8):
    print(n, factorial_function(n))


#You can use recursive functions in Python to write clean, elegant code, and divide it into smaller, organized chunks. On the other hand, you need to be very careful as it might be easy to make a mistake and create a function which never terminates. You also need to remember that recursive calls consume a lot of memory, and therefore may sometimes be inefficient.

# When using recursion, you need to take all its advantages and disadvantages into consideration.

# The factorial function is a classic example of how the concept of recursion can be put in practice:
# Recursive implementation of the factorial function.

def factorial(n):
    if n == 1:    # The base case (termination condition.)
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4)) # 4 * 3 * 2 * 1 = 24


#Question 1: What will happen when you attempt to run the following snippet and why?
def factorial(n):
    return n * factorial(n - 1)

print(factorial(4))
#The factorial function has no termination condition (no base case) so Python will raise an exception (RecursionError: maximum recursion depth exceeded)
