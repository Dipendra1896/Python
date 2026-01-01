# num1 = 5

# while num1<=10:
#     print("I am stuck inside a loop")
#     num1 += 1

# Store the current largest number here.
# largest_number = -999999999

# # Input the first value.
# number = int(input("Enter a number or type -1 to stop: "))

# # If the number is not equal to -1, continue.
# while number != -1:
#     # Is number larger than largest_number?
#     if number > largest_number:
#         # Yes, update largest_number.
#         largest_number = number
#     # Input the next number.
#     number = int(input("Enter a number or type -1 to stop: "))

# # Print the largest number.
# print("The largest number is:", largest_number)


# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

# odd_numbers = 0
# even_numbers = 0

# # Read the first number.
# number = int(input("Enter a number or type 0 to stop: "))

# # 0 terminates execution.
# while number != 0:
#     # Check if the number is odd.
#     if number % 2 == 1:
#         # Increase the odd_numbers counter.
#         odd_numbers += 1
#     else:
#         # Increase the even_numbers counter.
#         even_numbers += 1
#     # Read the next number.
#     number = int(input("Enter a number or type 0 to stop: "))

# # Print results.
# print("Odd numbers count:", odd_numbers)
# print("Even numbers count:", even_numbers)

# counter = 5
# while counter != 0:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)

# counter = 5
# while counter:
#     print("Inside the loop.", counter)
#     counter -= 1
# print("Outside the loop.", counter)


# secret_number = 777

# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)
# num1 = int(input("Enter the 3 digit secret number: "))
# while num1 != secret_number:
#     print("Ha ha! You're stuck in my loop!")
#     num1 = int(input("Enter the number: "))
# print("Well done, muggle! You are free now.")

# Looping with for loop
# i = 0
# while i < 100:
#     print("Current value of i :", i)
#     i += 1
# print(""" +============+""")
# for i in range(100):
#     print("Current value of i :", i)
  

# range function with two arguments
# for i in range(2,8):  # here i starts with initial value 2 and goes until 7
#     print("Current value of i :", i) 

# range function with three arguments
for i in range(2,8,2):  # here i starts with initial value 2 and goes to 6 with an increment of 2 : 2, 4, 6
    print("Current value of i :", i) 
