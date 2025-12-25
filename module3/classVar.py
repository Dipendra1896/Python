class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

# O/P:
# {'_ExampleClass__first': 1} 3
# {'_ExampleClass__first': 2} 3
# {'_ExampleClass__first': 4} 3

# Two important conclusions come from the example:

# class variables aren't shown in an object's __dict__ (this is natural as class variables aren't parts of an object) but you can always try to look into the variable of the same name, but at the class level – we'll show you this very soon;
# a class variable always presents the same value in all class instances (objects)

# | Concept                       | Meaning                                              |
# | ----------------------------- | ---------------------------------------------------- |
# | Class variable                | Belongs to the class                                 |
# | Instance variable             | Belongs to an object                                 |
# | Stored in object’s `__dict__` | Only instance variables                              |
# | Shared value                  | Class variable is the same for all objects           |
# | Override                      | Assigning via object creates a new instance variable |



class ExampleClass:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.__counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
print(example_object_3.__dict__, example_object_3._ExampleClass__counter)


# Now we're going to take the opportunity to show you the difference between these two __dict__ variables, the one from the class and the one from the object.

class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val


print(ExampleClass.__dict__)
example_object = ExampleClass(2)

print(ExampleClass.__dict__)
print(example_object.__dict__)

# Let's take a closer look at it:

# We define one class named ExampleClass;

# The class defines one class variable named varia;

# The class constructor sets the variable with the parameter's value;

# Naming the variable is the most important aspect of the example because:
# Changing the assignment to self.varia = val would create an instance variable of the same name as the class's one;
# Changing the assignment to varia = val would operate on a method's local variable; (we strongly encourage you to test both of the above cases - this will make it easier for you to remember the difference)
# The first line of the off-class code prints the value of the ExampleClass.varia attribute; note – we use the value before the very first object of the class is instantiated.




#checking attribute existence
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a)
print(example_object.b)
    
# As you can see, accessing a non-existing object (class) attribute causes an AttributeError exception.

# The try-except instruction gives you the chance to avoid issues with non-existent properties.

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)

try:
    print(example_object.b)
except AttributeError:
    pass
    


# Python provides a function which is able to safely check if any object/class contains a specified property. The function is named hasattr, and expects two arguments to be passed to it:

# the class or the object being checked;
# the name of the property whose existence has to be reported (note: it has to be a string containing the attribute name, not the name alone)
# The function returns True or False.

# This is how you can utilize it:

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1
 
 
example_object = ExampleClass(1)
print(example_object.a)
 
if hasattr(example_object, 'b'):
    print(example_object.b)


# Don't forget that the hasattr() function can operate on classes, too. You can use it to find out if a class variable is available, just like here in the example in the editor.

class ExampleClass:
    attr = 1


print(hasattr(ExampleClass, 'attr'))
print(hasattr(ExampleClass, 'prop'))
    

# Example2:
class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2


example_object = ExampleClass()

print(hasattr(example_object, 'b'))
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))



