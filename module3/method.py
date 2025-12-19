# A method is a function embedded inside a class.

# There is one fundamental requirement – a method is obliged to have at least one parameter(usually :self  recommended.it identifies the object for which the method is invoked.)
#E.g1
# class Classy:
#     def method(self):
#         print("method")


# obj = Classy()
# obj.method()
    
# # E.g2
# class Classy:
#     def method(self, par):
#         print("method:", par)
 
 
# obj = Classy()
# obj.method(1)
# obj.method(2)
# obj.method(3)
 

#The self parameter is used to obtain access to the object's instance and class variables.
# class Classy:
#     varia = 2
#     def method(self):
#         print(self.varia, self.var)


# obj = Classy()
# obj.var = 3
# obj.method()

#The self parameter is also used to invoke other object/class methods from inside the class.
# class Classy:
#     def other(self):
#         print("other")
 
#     def method(self):
#         print("method")
#         self.other()
 
 
# obj = Classy()
# obj.method()
 

# The constructor:

# is obliged to have the self parameter (it's set automatically, as usual)
# may (but doesn't need to) have more parameters than just self; if this happens, the way in which the class name is used to create the object must reflect the __init__ definition;
# can be used to set up the object, i.e., properly initialize its internal state, create instance variables, instantiate any other objects if their existence is needed, etc.

# class Classy:
#     def __init__(self, value):
#         self.var = value


# obj_1 = Classy("object")

# print(obj_1.var)

# Note that the constructor:

# cannot return a value, as it is designed to return a newly created object and nothing else;
# cannot be invoked directly either from the object or from inside the class (you can invoke a constructor from any of the object's subclasses, but we'll discuss this issue later.)

# As __init__ is a method, and a method is a function, you can do the same tricks with constructors/methods as you do with ordinary functions.The example in the editor shows how to define a constructor with a default argument value. Test it.

# class Classy:
#     def __init__(self, value = None):
#         self.var = value


# obj_1 = Classy("object")
# obj_2 = Classy()

# print(obj_1.var)
# print(obj_2.var)
    

# Everything we've said about property name mangling applies to method names, too – a method whose name starts with __ is (partially) hidden.

# class Classy:
#     def visible(self):
#         print("visible")

#     def __hidden(self):
#         print("hidden")


# obj = Classy()
# obj.visible()

# try:
#     obj.__hidden()
# except:
#     print("failed")

# obj._Classy__hidden()

# 3.4.2 The inner life of classes and objects
# Each Python class and each Python object is pre-equipped with a set of useful attributes which can be used to examine its capabilities.

# You already know one of these – it's the __dict__ property.

# class Classy:
#     varia = 1
#     def __init__(self):
#         self.var = 2

#     def method(self):
#         pass

#     def __hidden(self):
#         pass


# obj = Classy()

# print(obj.__dict__)
# print(Classy.__dict__)
    

# If you want to find the class of a particular object, you can use a function named type(), which is able (among other things) to find a class which has been used to instantiate any object.

# Look at the code in the editor, run it, and see for yourself.
# class Classy:
#     pass


# print(Classy.__name__)
# obj = Classy()
# print(type(obj).__name__)
    
# print(obj.__name__)  #Note that a statement like this will cause an error

#__module__ is a string, too – it stores the name of the module which contains the definition of the class.

# class Classy:
#     pass


# print(Classy.__module__)
# obj = Classy()
# print(obj.__module__)

# O/P: 
# __main__
# __main__      As you know, any module named __main__ is actually not a module, but the file currently being run.



# __bases__ is a tuple. The tuple contains classes (not class names) which are direct superclasses for the class.
# The order is the same as that used inside the class definition.
# We'll show you only a very basic example, as we want to highlight how inheritance works.
# Moreover, we're going to show you how to use this attribute when we discuss the object approach aspects of exceptions.
# Note: only classes have this attribute – objects don't.
# We've defined a function named printbases(), designed to present the tuple's contents clearly.

class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)

# __bases__ is a tuple that tells you which classes a class directly inherits from, which is why SuperOne and SuperTwo show object, while Sub shows both parent classes.
#Note:
#If you create a class and don’t explicitly say what it inherits from, Python automatically makes it inherit from object.
# class MyClass:
#     pass
# #is actually treated by Python as:
# class MyClass(object):
#     pass
# print(MyClass.__bases__)