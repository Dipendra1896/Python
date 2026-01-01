# def message():
#     print("Enter a value:")
#     a = int(input())
#     print(a)

# print("We start here.")
# message()
# print("We stop here")


# def hello(name):    # defining a function
#     print("Hello,", name)    # body of the function


# name = input("Enter your name: ")

# hello(name)    # calling the function


# def message(what, number):
#     print("Enter", what, "number", number)

# message("telephone", 11)
# message("price", 5)

# def get(num1, num2):
#     sum = 0
#     sum = num1 + num2
#     if sum % 2 == 0:
#         print("Even")
#     else: 
#         print("odd")
# print("Enter two numbers:")
# a = int(input())
# b = int(input())
# get(a,b)

# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)

# print("Enter your first name:")
# first_name = input()
# print("Enter your last name:")
# last_name = input()
# introduction(first_name, last_name)


# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)

# introduction(first_name = "Dipendra", last_name = "Patel")
# introduction(last_name = "Patel", first_name = "Dipendra")

# def adding(a, b, c):
#     print(a, "+", b, "+", c, "=" , a+b+c)
# adding(a=2, b=4, c=6)
# adding(c=2, b=4, a=6)
# adding(c=2, a=4, b=6)

# def introduction(first_name, last_name="Patel"):
#      print("Hello, my name is", first_name, last_name)

# introduction("Rajat", "Yadav")  # outputs Hello, my name is Rajat Yadav
# introduction("Dipak")         #outputs Hello, my name is Dipak Patel
# introduction(first_name="Dipendra") #Outputs Hello, my name is Dipendra Patel

def introduction(first_name = "Dipendra", last_name = "Patel"):
     print("Hello, my name is", first_name, last_name)
introduction()
introduction(last_name="Raut")
introduction(first_name="Dipak")


