# A Python generator is a piece of specialized code able to produce a series of values, and to control the iteration process. This is why generators are very often called iterators, and although some may find a very subtle distinction between these two, we'll treat them as one.

for i in range(5):
    print(i)

# The range() function is, in fact, a generator, which is (in fact, again) an iterator.
#A generator returns a series of values, and in general, is (implicitly) invoked more than once.

# The iterator protocol is a way in which an object should behave to conform to the rules imposed by the context of the for and in statements. An object conforming to the iterator protocol is called an iterator.
# An iterator must provide two methods:
# __iter__() which should return the object itself and which is invoked once (it's needed for Python to successfully start the iteration)
# __next__() which is intended to return the next value (first, second, and so on) of the desired series – it will be invoked by the for/in statements in order to pass through the next iteration; if there are no more values to provide, the method should raise the StopIteration exception.
class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")		
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)
    


class Fib:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("Fib iter")
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print("Class iter")
        return self.__iter


object = Class(8)

for i in object:
    print(i)
    

# #The yield statement:You may think of the yield keyword as a smarter sibling of the return statement, with one essential difference.
def fun(n):
    for i in range(n):
        return i

def fun(n):
      for i in range(n):
         yield i


#How to build a generator
def fun(n):
    for i in range(n):
        yield i


for v in fun(5):
    print(v)

# a generator to produce the first n powers of 2
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v)



#List comprehensions:Generators may also be used within list comprehensions, just like here:

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 
t = [x for x in powers_of_2(5)]
print(t)



#The list() function: The list() function can transform a series of subsequent generator invocations into a real list:
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 
t = list(powers_of_2(3))
print(t)



# The in operator
# Moreover, the context created by the in operator allows you to use a generator, too.
# # The example shows how to do it:
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 
for i in range(20):
    if i in powers_of_2(4):
        print(i)
 
# The fibonacci Number Generator:
def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(10))
print(fibs)

# More about list comprehensions
list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]

print(list_1)
print(list_2)
    


the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)
    
# Same gaol can be achieved in following way also:
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
print(the_list)

# List comprehensions vs. generators: Just one change can turn any list comprehension into a generator.It's the parentheses. The brackets make a comprehension, the parentheses make a generator.Look the example :

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))   #parentheses

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()


