class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass 

class TrackedVehicle(LandVehicle):
    pass

for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end = "\t")
    print()        



# isinstance() method: identify whether it is an onject of a class or not

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()
    
# The is operator: The is operator checks whether two variables (object_one and object_two here) refer to the same objects. Syntax:  object_one is object_two
# Don't forget that variables don't store the objects themselves, but only the handles pointing to the internal Python memory.

class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1
object_3.val += 1

print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print(string_1 == string_2, string_1 is string_2)


# How Python finds properties and methods
class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)


obj = Sub("Andy")

print(obj)

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
class Super:
    supVar = 1


class Sub(Super):
    subVar = 2


obj = Sub()

print(obj.subVar)
print(obj.supVar)


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

#The example in the editor summarizes this in a three-level inheritance line. Analyze it carefully.
class Level1:
    variable_1 = 100
    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102


class Level2(Level1):
    variable_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201
    
    def fun_2(self):
        return 202


class Level3(Level2):
    variable_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302


obj = Level3()

print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())
    
# multiple inheritance:Multiple inheritance occurs when a class has more than one superclass. Syntactically, such inheritance is presented as a comma-separated list of superclasses put inside parentheses after the new class name – just like here:
class SuperA:
    var_a = 10
    def fun_a(self):
        return 11
 
 
class SuperB:
    var_b = 20
    def fun_b(self):
        return 21
 
 
class Sub(SuperA, SuperB):
    pass
 
obj = Sub()
 
print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())

# overriding:
class Level1:
    var = 100
    def fun(self):
        return 101


class Level2(Level1):
    var = 200
    def fun(self):
        return 201


class Level3(Level2):
    pass


obj = Level3()

print(obj.var, obj.fun())

#Both, Level1 and Level2 classes define a method named fun() and a property named var. Does this mean that the Level3 class object will be able to access two copies of each entity? Not at all.
#The entity defined later (in the inheritance sense) overrides the same entity defined earlier. This is why the code produces the following output:  200  201


class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"


class Sub(Left, Right):
    pass


obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())
    

# The Sub class inherits goods from two superclasses, Left and Right.

# There is no doubt that the class variable var_right comes from the Right class, and var_left comes from Left respectively.

# This is clear. But where does var come from? Is it possible to guess it? The same problem is encountered with the fun() method – will it be invoked from Left or from Right?
#Output: L LL RR Left

# We can say that Python looks for object components in the following order:

# inside the object itself;
# in its superclasses, from bottom to top;
# if there is more than one class on a particular inheritance path, Python scans them from left to right.

#  Do you need anything more? Just make a small amendment in the code – replace: class Sub(Left, Right): with: class Sub(Right, Left):, then run the program again, and see what happens.
#Output: R LL RR Right

# How to build a hierarchy of classes

class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it from Two")


one = One()
two = Two()

one.doanything()
two.doanything()


# Let's analyze it:

# there are two classes, named One and Two, while Two is derived from One. Nothing special. However, one thing looks remarkable - the do_it() method.the do_it()method is defined twice: originally inside One and subsequently inside Two. The essence of the example lies in the fact that it is invoked just once – inside One.The question is – which of the two methods will be invoked by the last two lines of the code?


# The first invocation seems to be simple, and it is simple, actually – invoking doanything() from the object named one will obviously activate the first of the methods.The second invocation needs some attention. It's simple, too if you keep in mind how Python finds class components. The second invocation will launch do_it() in the form existing inside the Two class, regardless of the fact that the invocation takes place within the One class.

#Note: the situation in which the subclass is able to modify its superclass behavior (just like in the example) is called polymorphism. The word comes from Greek (polys: "many, much" and morphe, "form, shape"), which means that one and the same class can take various forms depending on the redefinitions done by any of its subclasses.

#We're going to show you how to use polymorphism to extend class flexibility.
import time

class Vehicle:
    def change_direction(left, on):
        pass

    def turn(left):
        change_direction(left, True)
        time.sleep(0.25)
        change_direction(left, False)


class TrackedVehicle(Vehicle):
    def control_track(left, stop):
        pass

    def change_direction(left, on):
        control_track(left, on)


class WheeledVehicle(Vehicle):
    def turn_front_wheels(left, on):
        pass

    def change_direction(left, on):
        turn_front_wheels(left, on)
        
    

# Composition is the process of composing an object using other different objects. The objects used in the composition deliver a set of desired traits (properties and/or methods) so we can say that they act like blocks used to build a more complicated structure.

# It can be said that:

# inheritance extends a class's capabilities by adding new components and modifying existing ones; in other words, the complete recipe is contained inside the class itself and all its ancestors; the object takes all the class's belongings and makes use of them;
# composition projects a class as a container able to store and use other objects (derived from other classes) where each of the objects implements a part of a desired class's behavior.





#What is Method Resolution Order (MRO): It is a strategy in which a particular programming langusge scans through the upper part of a class's hierarchy in order to find the method it currently needs.

class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

# Lets make a little bit changes:
class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Middle, Top):   
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()
    
#lets  change the order of superclass in Bottom(Middle,Top) to Bottom(Top,Middle)
class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Top, Middle):     # cause MRO rule breaked here
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()
    

class Top:
    def m_top(self):
        print("top")


class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")


class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")


class Bottom(Middle_Left, Middle_Right):
	def m_bottom(self):
		print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

# Note: both Middle classes define a method of the same name: m_middle().

# It introduces a small uncertainty to our sample, although we're absolutely sure that you can answer the following key question: which of the two m_middle() methods will actually be invoked when the following line is executed?:Object.m_middle()
 
#In other words, what will you see on the screen: middle_left or middle_right?
# You don't need to hurry – think twice and keep Python's MRO in mind!
# Yes, you're right. The invocation will activate the m_middle() method, which comes from the Middle_Left class. The explanation is simple: the class is listed before Middle_Right on the Bottom class's inheritance list. If you want to make sure that there’s no doubt about it, try to swap these two classes on the list and check the results.



class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def __str__(self):
        return self.breed + " says: Woof!"


class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " Don't run away, Little Lamb!"


class GuardDog(Dog):
    def __str__(self):
        return super().__str__() + " Stay where you are, Mister Intruder!"


rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")

