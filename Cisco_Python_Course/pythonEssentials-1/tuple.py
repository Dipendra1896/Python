# A tuple is an immutable sequence type. It can behave like a list, but it can't be modified in situ.
# The first and the clearest distinction between lists and tuples is the syntax used to create them - tuples prefer to use parenthesis, whereas lists like to see brackets, although it's also possible to create a tuple just from a set of values separated by commas.Look at the example:
tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
tuple3 = 1, 2, 3

print(tuple_1)
print(tuple_2)
print(tuple3)

#Note: each tuple element may be of a different type (floating-point, integer, or any other not-as-yet-introduced kind of data).

# How to create a tuple??
# It is possible to create an empty tuple – parentheses are required then: empty_tuple = ()
 
# If you want to create a one-element tuple, you have to take into consideration the fact that, due to syntax reasons (a tuple has to be distinguishable from an ordinary, single value), you must end the value with a comma:

# one_element_tuple_1 = (1, )
# one_element_tuple_2 = 1.,



# The similarities may be misleading − don't try to modify a tuple's contents! It's not a list!

# All of these instructions (except the topmost one) will cause a runtime error:

# my_tuple = (1, 10, 100, 1000)
 
# my_tuple.append(10000)
# del my_tuple[0]
# my_tuple[1] = -10
 
# This is the message that Python will give you in the console window:

# Output
# AttributeError: 'tuple' object has no attribute 'append'
# What else can tuples do for you?

# the len() function accepts tuples, and returns the number of elements contained inside;
# the + operator can join tuples together (we've shown you this already)
# the * operator can multiply tuples, just like lists;
# the in and not in operators work in the same way as in lists.
#The snippet in the editor presents them all.
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

# This is what you should see in the console:
# 9
# (1, 10, 100, 1000, 10000)
# (1, 10, 100, 1, 10, 100, 1, 10, 100)
# True
# True


# One of the most useful tuple properties is their ability to appear on the left side of the assignment operator. You saw this phenomenon some time ago, when it was necessary to find an elegant tool to swap two variables' values.

# Take a look at the snippet below:
var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

# It shows three tuples interacting − in effect, the values stored in them "circulate" − t1 becomes t2, t2 becomes t3, and t3 becomes t1.

# Note: the example presents one more important fact: a tuple's elements can be variables, not only literals. Moreover, they can be expressions if they're on the right side of the assignment operator.