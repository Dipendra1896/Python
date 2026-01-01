# def is_a_triangle(a,b,c):
#     if a+b <= c:
#         return False
#     if b+c <= a:
#         return False
#     if c+a <= b:
#         return False
#     return True

# print(is_a_triangle(1,1,2))
# print(is_a_triangle(2,2,3))
 
#  #more compact way for triangle formation checking
 
# def is_a_triangle(a,b,c):
#     if a+b <= c or b+c <= a or c+a <= b:
#         return False
#     return True

# print(is_a_triangle(1,1,2))
# print(is_a_triangle(2,2,3))

# # More compact version of this can be 
# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# print(is_a_triangle(1, 1, 2))
# print(is_a_triangle(2, 2, 3))
 
#lets ask the user for three values and make use of the function.
# def is_a_triangle(a,b,c):
#     return a+b > c and b+c > a and c+a > b
# a = float(input('Enter the first side\'s length:'))
# b = float(input('Enter the second side\'s length:'))
# c = float(input('Enter the third side\'s length:'))

# if is_a_triangle(a,b,c):
#     print('Yes, it can be a triangle.')
# else:
#     print('No,it can\'t be a triangle.') 

#Right angle triangle checking

# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# def is_a_right_triangle(a, b, c):
#     if not is_a_triangle(a, b, c):
#         return False
#     if c > a and c > b:
#         return c ** 2 == a ** 2 + b ** 2
#     if a > b and a > c:
#         return a ** 2 == b ** 2 + c ** 2
#     if b > a and b > c:
#         return b ** 2 == a ** 2 + c ** 2
# print(is_a_right_triangle(5, 3, 4)) #true
# print(is_a_right_triangle(1, 3, 4)) # false
# print(is_a_right_triangle(3, 5, 4)) #true

#Evaluating a triangle's area
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
def area_of_triangle(a, b, c):
    print("Heron formula result (even if not a triangle):", heron(a, b, c))
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)

print(area_of_triangle(1., 1., 2. ** .5)) #o/p :0.49999999999999983
print(area_of_triangle(2, 3, 6))    #o/p :none
print(area_of_triangle(1 , 1, 2 **5))

#  OUTPUTS:
# Heron formula result (even if not a triangle): 0.49999999999999983
# 0.49999999999999983
# Heron formula result (even if not a triangle): (3.0036631706260336e-16+4.905354217587146j)
# None
# It is printed 0.49999999999999983  It's very close to 0.5, but it isn't exactly 0.5. What does it mean? Is it an error?
# No, it isn't. This is the specifics of floating-point calculations.