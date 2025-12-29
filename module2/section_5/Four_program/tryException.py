# try:
#     print("1")
#     x = 1 / 0
#     print("2")
# except:
#     print("Oh dear, something went wrong...")

# print("3")
    

# try:
#     x = int(input("Enter a number: "))
#     y = 1 / x
# except:
#     print("Oh dear, something went wrong...")

# print("THE END.")    

# try:
#     x = int(input("Enter a number: "))
#     y = 1 / x
#     print(y)
# except ZeroDivisionError:
#     print("You cannot divide by zero, sorry.")
# except ValueError:
#     print("You must enter an integer value.")
# except:
#     print("Oh dear, something went wrong...")

# print("THE END.")
    

# try:
#     y = 1 / 0
# except ZeroDivisionError:
#     print("Ooopsss...")

# print("THE END.")
    

# try:
#     y = 1 / 0
# except ArithmeticError: # ZeroDivisionError is special case of more general class named ArithmeticError so the o/p remains same as zeroDivisionError
#     print("Oooppsss...")
 
# print("THE END.")    

# Something has changed in it - we've replaced ZeroDivisionError with ArithmeticError.

# You already know that ArithmeticError is a general class including (among others) the ZeroDivisionError exception.

# Thus, the code's output remains unchanged. Test it.

# This also means that replacing the exception's name with either Exception or BaseException won't change the program's behavior.



# x = '\''
# print(len(x))

# print(ord('c') - ord('a'))

print(chr(ord('z') - 2))

print(3 * 'abc' + 'xyz')

print('Mike' > "Mikey")

print(float("1, 3"))

