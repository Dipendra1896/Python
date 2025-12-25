# Using dir() Function:
# The function returns an alphabetically sorted list containing all entities' names available in the module identified by a name passed to the function as an argument:


import math
for name in dir(math):
    print(name, end="\t")


#Exploring math module in a little bit depth
from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)
print(ar)
print(ad)

 # math module also contains a set of their hyperbolic analogues:
# sinh(x) → the hyperbolic sine;
# cosh(x) → the hyperbolic cosine;
# tanh(x) → the hyperbolic tangent;
# asinh(x) → the hyperbolic arcsine;
# acosh(x) → the hyperbolic arccosine;
# atanh(x) → the hyperbolic arctangent.

# Another group of the math's functions is formed by functions which are connected with exponentiation:

# e → a constant with a value that is an approximation of Euler's number (e)
# exp(x) → finding the value of ex
# log(x) → the natural logarithm of x
# log(x, b) → the logarithm of x to base b
# log10(x) → the decimal logarithm of x (more precise than log(x, 10))
# log2(x) → the binary logarithm of x (more precise than log(x, 2))

from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))


# The last group consists of some general-purpose functions like:

# ceil(x) → the ceiling of x (the smallest integer greater than or equal to x)
# floor(x) → the floor of x (the largest integer less than or equal to x)
# trunc(x) → the value of x truncated to an integer (be careful - it's not an equivalent either of ceil or floor)
# factorial(x) → returns x! (x has to be an integral and not a negative)
# hypot(x, y) → returns the length of the hypotenuse of a right-angle triangle with the leg lengths equal to x and y (the same as sqrt(pow(x, 2) + pow(y, 2)) but more precise)



# Randomness 
# using module named: random 
# The randrange and randint functions
# If you want integer random values, one of the following functions would fit better:

# randrange(end)
# randrange(beg, end)
# randrange(beg, end, step)
# randint(left, right)

from random import randrange, randint

print(randrange(1), end='\n')
print(randrange(0, 1), end='\n')
print(randrange(0, 1, 1), end='\n')
print(randint(0, 1))

from random import randint

for i in range(10):
    print(randint(1, 10), end=',')

# Platform module
from platform import platform

print(platform())     #platform() function
print(platform(1))
print(platform(0, 1))

from platform import machine

print(machine())    #machine() function


from platform import processor

print(processor())   # processor() function

from platform import system

print(system())  # system() function return generic os name as string


from platform import version

print(version())  # version() returns os version 

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)


import os
dir(os)
