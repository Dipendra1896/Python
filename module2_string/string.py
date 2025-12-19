# multiline = '''Line #1
# Line #2'''
# print(len(multiline))


# multiline = """Line #1
# Line #2"""
# print(len(multiline))

# str1 = 'a'
# str2 = 'b'

# print(str1 + str2)
# print(str2 + str1)
# print(5 * 'a')
# print('b' * 4)

# ord(): returns specific character ASCII/ UNICODE
# char_1 = 'A'
# char_2 = '@' #space

# print(ord(char_1))
# print(ord(char_2))

# chr(): If you know the code point (number) and want to get the corresponding character, you can use a function named chr().The function takes a code point and returns its character.
# Demonstrating the chr() function.

# print(chr(97))
# print(chr(945))

# String as sequence : Indexing
# Indexing strings.

# the_string = 'silly walks'

# for ix in range(len(the_string)):
#     print(the_string[ix], end=' ')

# print()


# the_string = 'silly walks'

# for ix in range(len(the_string)):
#     print(the_string[-ix], end=' ')

# print()

#Iterating
# Iterating through a string.

# the_string = 'silly walks'

# for character in the_string:
#     print(character, end=' ')

# print()


#Slicing
# Slices

# alpha = "Dipendra"

# print(alpha[1:3])
# print(alpha[3:])
# print(alpha[:3])
# print(alpha[3:-2])
# print(alpha[-3:4])
# print(alpha[::2])
# print(alpha[1::2])


#The in and not in operators:
# alphabet = "Dipendar Patel"

# print("D" in alphabet)
# print("r" in alphabet)
# print("1" in alphabet)
# print("dra" in alphabet)
# print("tel" in alphabet)

# alphabet = "Dipendra Patel"

# print("D" not in alphabet)
# print("r" not in alphabet)
# print("1" not in alphabet)
# print("dra" not in alphabet)
# print("tel" not in alphabet)


# Python string are immutable
# alphabet = "bcdefghijklmnopqrstuvwxy"
# alphabet_1 = "Dipendra"
# alphabet = "a" + alphabet
# alphabet = alphabet + "z"
# alphabet_1 = alphabet_1 + " Patel"
# print(alphabet)
# print(alphabet_1)

# Demonstrating max() - Example 1:
# print(max("aAbByYzZ"))


# Demonstrating max() - Examples 2 & 3:
# t = 'The Knights Who Say "Ni!"'
# print('[' + max(t) + ']')

# t = [0, 1, 2]
# print(max(t))

# index(), count() methods, & list() function

# print("Dipendra".index("e"))    # outputs index of the character
# print("DipendraDip".count("i"))  # counts the occurrence of the character
# print(list("Dipendra"))      #creates new list containing all the characters, one per list elements

# #capitalize() method
# print("diPeNdrA".capitalize())  #o/p: Dipendra
# print("Alpha".capitalize())
# print('ALPHA'.capitalize())
# print(' Alpha'.capitalize())
# print('123'.capitalize())
# print("αβγδ".capitalize())


# Demonstrating the endswith() method: checks if the string ends with the specified argument
# if "epsilon".endswith("on"):
#     print("yes")
# else:
#     print("no")

# Demonstrating the find() method: similar to index() but it does not return error for non-existent substring
# print("Eta".find("ta"))
# print("Eta".find("mma"))
# Note: don't use find() if you only want to check if a single character occurs within a string - the in operator will be significantly faster.
#e.g1:
# t = 'theta'
# print(t.find('eta'))
# print(t.find('et'))
# print(t.find('the'))
# print(t.find('ha'))
#e.g2:
# print('kappa'.find('a', 2))
# e.g3:
# the_text = """A variation of the ordinary lorem ipsum
# text has been used in typesetting since the 1960s 
# or earlier, when it was popularized by advertisements 
# for Letraset transfer sheets. It was introduced to 
# the Information Age in the mid-1980s by the Aldus Corporation, 
# which employed it in graphics and word-processing templates
# for its desktop publishing program PageMaker (from Wikipedia)"""

# fnd = the_text.find('the')
# while fnd != -1:
#     print(fnd)
#     fnd = the_text.find('the', fnd + 1)


# isalnum():The parameterless method named isalnum() checks if the string contains only digits or alphabetical characters (letters), and returns True or False according to the result.

# Demonstrating the isalnum() method:
# print('lambda30'.isalnum())
# print('lambda'.isalnum())
# print('30'.isalnum())
# print('@'.isalnum())
# print('lambda_30'.isalnum())
# print(''.isalnum())

# t = 'Six lambdas'
# print(t.isalnum())

# t = '&Alpha;&beta;&Gamma;&delta;'
# print(t.isalnum())

# t = '20E1'
# print(t.isalnum())

# Example 1: Demonstrating the isapha() method:
# print("Moooo".isalpha())
# print('Mu40'.isalpha())

# # Example 2: Demonstrating the isdigit() method:
# print('2018'.isdigit())
# print("Year2019".isdigit())

# # Example: Demonstrating the islower() method:
# print("Moooo".islower())
# print('moooo'.islower())
    
# # Example: Demonstrating the isspace() method:
# print(' \n '.isspace())
# print(" ".isspace())
# print("mooo mooo mooo".isspace())

# Example: Demonstrating the isupper() method:
# print("Moooo".isupper())
# print('moooo'.isupper())
# print('MOOOO'.isupper())

# # Demonstrating the join() method:
# print("_".join(["Dipendra", "Raut", "Kurmi"]))


# # Demonstrating the lower() method:
# print("SiGmA=60".lower())


# Demonstrating the lstrip() method:
# print("[" + "tau ".lstrip() + "]")
# st = "     _Dipendra patel "
# print("[" + st.lstrip()+"]")

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
print(s2)
print(s2[-2])
