#instance Variable

class ExampleClass:
    def __init__(self, val = 1):
        self.first = val
 
    def set_second(self, val):
        self.second = val
 
 
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
 
example_object_2.set_second(3)
 
example_object_3 = ExampleClass(4)
example_object_3.third = 5
 
print(example_object_1.__dict__)    #{'first': 1}
print(example_object_2.__dict__)    #{'first': 2, 'second': 3}
print(example_object_3.__dict__)    #{'first': 4, 'third': 5}



# There is one additional conclusion that should be stated here: modifying an instance variable of any object has no impact on all the remaining objects. Instance variables are perfectly isolated from each other.

class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5


print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

# O/P:   
# {'_ExampleClass__first': 1}
# {'_ExampleClass__first': 2, '_ExampleClass__second': 3}
# {'_ExampleClass__first': 4, '__third': 5}

# Can you see these strange names full of underscores? Where did they come from?

# When Python sees that you want to add an instance variable to an object and you're going to do it inside any of the object's methods, it mangles the operation in the following way:

#  -> it puts a class name before your name;
#  -> it puts an additional underscore at the beginning.
#  -> This is why the __first becomes _ExampleClass__first.


# The name is now fully accessible from outside the class. You can run a code like this:

print(example_object_1._ExampleClass__first)

# The mangling won't work if you add a private instance variable outside the class code. In this case, it'll behave like any other ordinary property.