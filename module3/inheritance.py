# class Vehicle:
#     pass

# class LandVehicle(Vehicle):
#     pass 

# class TrackedVehicle(LandVehicle):
#     pass

# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
#     for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(issubclass(cls1, cls2), end = "\t")
#     print()        



# isinstance() method: identify whether it is an onject of a class or not

# class Vehicle:
#     pass


# class LandVehicle(Vehicle):
#     pass


# class TrackedVehicle(LandVehicle):
#     pass


# my_vehicle = Vehicle()
# my_land_vehicle = LandVehicle()
# my_tracked_vehicle = TrackedVehicle()

# for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
#     for cls in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(isinstance(obj, cls), end="\t")
#     print()
    
# The is operator: The is operator checks whether two variables (object_one and object_two here) refer to the same objects. Syntax:  object_one is object_two
# Don't forget that variables don't store the objects themselves, but only the handles pointing to the internal Python memory.

# class SampleClass:
#     def __init__(self, val):
#         self.val = val


# object_1 = SampleClass(0)
# object_2 = SampleClass(2)
# object_3 = object_1
# object_3.val += 1

# print(object_1 is object_2)
# print(object_2 is object_3)
# print(object_3 is object_1)
# print(object_1.val, object_2.val, object_3.val)

# string_1 = "Mary had a little "
# string_2 = "Mary had a little lamb"
# string_1 += "lamb"

# print(string_1 == string_2, string_1 is string_2)


# How Python finds properties and methods
# class Super:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return "My name is " + self.name + "."


# class Sub(Super):
#     def __init__(self, name):
#         Super.__init__(self, name)


# obj = Sub("Andy")

# print(obj)

# Let's analyze it:

# there is a class named Super, which defines its own constructor used to assign the object's property, named name.
# the class defines the __str__() method, too, which makes the class able to present its identity in clear text form.
# the class is next used as a base to create a subclass named Sub. The Sub class defines its own constructor, which invokes the one from the superclass. Note how we've done it: Super.__init__(self, name).
# we've explicitly named the superclass, and pointed to the method to invoke __init__(), providing all needed arguments.
# we've instantiated one object of class Sub and printed it.
# Note: As there is no __str__() method within the Sub class, the printed string is to be produced within the Super class. This means that the __str__() method has been inherited by the Sub class.



# In the last example, we explicitly named the superclass. In this example, we make use of the super() function, which accesses the superclass without needing to know its name:
class SuperClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(SuperClass):
    def __init__(self, name):
        super().__init__(name)


obj = Sub("Andy")

print(obj)
    

# The super() function creates a context in which you don't have to (moreover, you mustn't) pass the self argument to the method being invoked – this is why it's possible to activate the superclass constructor using only one argument.

# Note: you can use this mechanism not only to invoke the superclass constructor, but also to get access to any of the resources available inside the superclass.

# Let's try to do something similar, but with properties (more precisely: with class variables).

# Take a look at the example in the editor.

# Testing properties: class variables.
# class Super:
#     supVar = 1


# class Sub(Super):
#     subVar = 2


# obj = Sub()

# print(obj.subVar)
# print(obj.supVar)


# As you can see, the Super class defines one class variable named supVar, and the Sub class defines a variable named subVar.

# Both these variables are visible inside the object of class Sub – this is why the code outputs: 2
  #                                                                                               1

# The same effect can be observed with instance variables – take a look at the second example in the editor.
# Testing properties: instance variables.
class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj = Sub()

print(obj.subVar)
print(obj.supVar)



# It's now possible to formulate a general statement describing Python's behavior.

# When you try to access any object's entity, Python will try to (in this order):


# find it inside the object itself;
# find it in all classes involved in the object's inheritance line from bottom to top;
# If both of the above fail, an exception (AttributeError) is raised.

