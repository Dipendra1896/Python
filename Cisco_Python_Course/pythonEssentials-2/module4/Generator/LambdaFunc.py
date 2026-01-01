# A lambda function is a function without a name (you can also call it an anonymous function).
# Syntax:
# lambda parameters: expression
#Such a clause returns the value of the expression when taking into account the current value of the current lambda argument.

#Example:
two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))


# Let's analzye it:

# the first lambda is an anonymous parameterless function that always returns 2. As we've assigned it to a variable named two, we can say that the function is not anonymous anymore, and we can use the name to invoke it.
# the second one is a one-parameter anonymous function that returns the value of its squared argument. We've named it as such, too.
# the third lambda takes two parameters and returns the value of the first one raised to the power of the second one. The name of the variable which carries the lambda speaks for itself. We don't use pow in order to avoid confusion with the built-in function of the same name and the same purpose.



#  How to use lambdas and what for?
def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)

# Let's analyze it. The print_function() function takes two parameters:

# the first, a list of arguments for which we want to print the results;
# the second, a function which should be invoked as many times as the number of values that are collected inside the first parameter.
# Note: we've also defined a function named poly() – this is the function whose values we're going to print. The calculation the function performs isn't very sophisticated – it's the polynomial (hence its name) of the form:

# f(x) = 2x2 - 4x + 2
# The name of the function is then passed to the print_function() along with a set of five different arguments – the set is built with a list comprehension clause.
#Can we avoid defining the poly() function, as we're not going to use it more than once? Yes, we can – this is the benefit a lambda can bring.
def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')
 
print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

#The print_function() has remained exactly the same, but there is no poly() function. We don't need it anymore, as the polynomial is now directly inside the print_function() invocation in the form of a lambda defined in the following way:
lambda x: 2 * x**2 - 4 * x + 2

# Another place where Lambda can be useful 
# Lambdas and the map() function:
#In the simplest of all possible cases, the map() function:

map(function, list)
#  It takes two arguments:

# -> a function;
# -> a list.
# The above description is extremely simplified, as:

# the second map() argument may be any entity that can be iterated (e.g., a tuple, or just a generator)
# map() can accept more than two arguments.
# The map() function applies the function passed by its first argument to all its second argument's elements, and returns an iterator delivering all subsequent function results.
#You can use the resulting iterator in a loop, or convert it into a list using the list() function.
 
#Uses of Lambda in map():
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()

# This is the intrigue:

# build the list_1 with values from 0 to 4;
# next, use map along with the first lambda to create a new list in which all elements have been evaluated as 2 raised to the power taken from the corresponding element from list_1;
# list_2 is printed then;
# in the next step, use the map() function again to make use of the generator it returns and to directly print all the values it delivers; as you can see, we've engaged the second lambda here – it just squares each element from list_2.



#Lambdas and the filter() function:It expects the same kind of arguments as map(), but does something different – it filters its second argument while being guided by directions flowing from the function specified as the first argument (the function is invoked for each list element, just like in map()).The elements which return True from the function pass the filter – the others are rejected.
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)
    
 
 
 #A brief look at closures:closure is a technique which allows the storing of values in spite of the fact that the context in which they have been created does not exist anymore.

def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())
    
# #A closure has to be invoked in exactly the same way in which it has been declared.
def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())

#Now look at the code in the editor. It is fully possible to declare a closure equipped with an arbitrary number of parameters, e.g., one, just like the power() function.
def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))
    