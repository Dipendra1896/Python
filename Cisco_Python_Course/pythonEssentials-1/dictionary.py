# The dictionary is another Python data structure. 
# It's not a sequence type (but can be easily adapted to sequence processing) and it is mutable.
#If you want to assign some initial pairs to a dictionary, you should use the following syntax:

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"} 
# phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
# empty_dictionary = {}  
 # The empty dictionary is constructed by an empty pair of curly braces 
 
# print(dictionary)
# print(phone_numbers)
# print(empty_dictionary)
# print(dictionary["cat"])

#The list of pairs is surrounded by curly braces, while the pairs themselves are separated by commas, and the keys and values by colons.
# A dictionary is a set of key-value pairs. Note:

# -> each key must be unique − it's not possible to have more than one key of the same value;
# -> a key may be any immutable type of object: it can be a number (integer or float), or even a string, but not a list;
# -> a dictionary is not a list − a list contains a set of numbered values, while a dictionary holds pairs of values;
# -> the len() function works for dictionaries, too − it returns the number of key-value elements in the dictionary;
# -> a dictionary is a one-way tool − if you have an English-French dictionary, you can look for French equivalents of English terms, but not vice versa.

# Note:

# if the key is a string, you have to specify it as a string;
# keys are case-sensitive: 'Suzy' is something different from 'suzy'.
# you mustn't use a non-existent key.

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
# words = ['cat', 'lion', 'horse']

# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print(word, "is not in dictionary")

# We can make the code more readable and programmer-friendly in following ways:
# Example 1:
# dictionary = {
#               "cat": "chat",
#               "dog": "chien",
#               "horse": "cheval"
# }
# # Example 2:
# phone_numbers = {'boss': 5551234567,
#               'Suzy': 22657854310
# }
# print(dictionary)
# print(phone_numbers)



 #The keys() method:
# The method returns an iterable object consisting of all the keys gathered within the dictionary. Having a group of keys enables you to access the whole dictionary in an easy and handy way.

# dictionary can be browsed like lists and tuples using for loop in following way:
# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

# for key in dictionary.keys():
#     print(key, "->", dictionary[key])

# The items() Method: The method returns tuples (this is the first example where tuples are something more than just an example of themselves) where each tuple is a key-value pair.

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

# for english, french in dictionary.items():
#     print(english, "->", french)

#Modifying and adding values: Assigning a new value to an existing key is simple.

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

# dictionary['cat'] = 'minou'
# print(dictionary)

# # For sorting the dictionary we can use sorted() function.
# for key in sorted(dictionary.keys()):
#     print(dictionary[key])

#There is also a method called values(), which works similarly to keys(), but returns values.
# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

# for french in dictionary.values():
#     print(french)

# Adding a new key:
# Adding a new key-value pair to a dictionary is as simple as changing a value – you only have to assign a value to a new, previously non-existent key. Note: this is very different behavior compared to lists, which don't allow you to assign values to non-existing indices.Let's add a new pair of words to the dictionary − a bit weird, but still valid:

# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

# dictionary['swan'] = 'cygne'
# print(dictionary)
 
#We can also insert an item to a dictionary by using the update() method, e.g.:
# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

# dictionary.update({"duck": "jemmy","parrot":"henna"})
# print(dictionary)

#Removing a key from dictionary: Note: removing a key will always cause the removal of the associated value. Values cannot exist without their keys. This is done with the del instruction.
#Example:
# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

# del dictionary['dog']  #delete the key 
# print(dictionary)


#To remove the last item in a dictionary, you can use the popitem() method:
# dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

# dictionary.popitem()
# print(dictionary)    # outputs: {'cat': 'chat', 'dog': 'chien'}

# Tuples and dictionaries can work together
# school_class = {}

# while True:
#     name = input("Enter the student's name: ")
#     if name == '':
#         break
    
#     score = int(input("Enter the student's score (0-10): "))
#     if score not in range(0, 11):
#         break
    
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
        
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)


# Summary Section
# -> 1. Tuples are ordered and unchangeable (immutable) collections of data. They can be thought of as immutable lists. They are written in round brackets:
#Each tuple element may be of a different type (i.e., integers, strings, booleans, etc.). What is more, tuples can contain other tuples or lists (and the other way round).
# my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
# print(my_tuple)

# my_list = [1, 2, True, "a string", (3, 4), [5, 6], None]
# print(my_list)

# -> 2. You can create an empty tuple like this:

# empty_tuple = ()
# print(type(empty_tuple)) # outputs: <class 'tuple'>

# -> 3. A one-element tuple may be created as follows:

# one_elem_tuple_1 = ("one", ) # Brackets and a comma.
# one_elem_tuple_2 = "one", # No brackets, just a comma.

# If you remove the comma, you will tell Python to create a variable, not a tuple:

# my_tuple_1 = 1,
# print(type(my_tuple_1)) # outputs: <class 'tuple'>
 
# my_tuple_2 = 1 # This is not a tuple.
# print(type(my_tuple_2)) # outputs: <class 'int'>

# -> 4. You can access tuple elements by indexing them:

# my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
# print(my_tuple[3]) # outputs: [3, 4]


# -> 6. You can loop through a tuple elements (Example 1), check if a specific element is (not)present in a tuple (Example 2), use the len() function to check how many elements there are in a tuple (Example 3), or even join/multiply tuples (Example 4):

# Example 1
# tuple_1 = (1, 2, 3)
# for elem in tuple_1:
#     print(elem)
 
# # Example 2
# tuple_2 = (1, 2, 3, 4)
# print(5 in tuple_2)
# print(5 not in tuple_2)
 
# # Example 3
# tuple_3 = (1, 2, 3, 4)
# print(len(tuple_3))
# print(5 not in tuple_3)
# # Example 4
# tuple_4 = tuple_1 + tuple_2
# tuple_5 = tuple_3 * 2
 
# print(tuple_4)
# print(tuple_5)


# You can also create a tuple using a Python built-in function called tuple(). This is particularly useful when you want to convert a certain iterable (e.g., a list, range, string, etc.) to a tuple:


# my_tuple = tuple((1, 2, "string"))
# print(my_tuple)
 
# my_list = [2, 4, 6]
# print(my_list) # outputs: [2, 4, 6]
# print(type(my_list)) # outputs: <class 'list'>
# tup = tuple(my_list)
# print(tup) # outputs: (2, 4, 6)
# print(type(tup)) # outputs: <class 'tuple'>

# By the same fashion, when you want to convert an iterable to a list, you can use a Python built-in function called list():

# tup = 1, 2, 3,
# my_list = list(tup)
# print(type(my_list)) # outputs: <class 'list'>


# Key takeaways: dictionaries
# -> 1. Dictionaries are unordered*, changeable (mutable), and indexed collections of data. (*Since Python 3.6x dictionaries have become ordered by default.)

# Each dictionary is a set of key: value pairs. You can create it by using the following syntax:


# my_dictionary = {
#     key1: value1,
#     key2: value2,
#     key3: value3,
# }


# -> 2. If you want to access a dictionary item, you can do so by making a reference to its key inside a pair of square brackets (ex. 1) or by using the get() method (ex. 2):


# pol_eng_dictionary = {
#     "kwiat": "flower",
#     "woda": "water",
#     "gleba": "soil"
#     }
 
# item_1 = pol_eng_dictionary["gleba"] # ex. 1
# print(item_1) # outputs: soil
 
# item_2 = pol_eng_dictionary.get("woda") # ex. 2
# print(item_2) # outputs: water

# ->  6. If you want to loop through a dictionary's keys and values, you can use the items() method, e.g.:


# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
#     }
 
# for key, value in pol_eng_dictionary.items():
#     print("Pol/Eng ->", key, ":", value)

# -> 7. To check if a given key exists in a dictionary, you can use the in keyword:


# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
#     }
 
# if "zamek" in pol_eng_dictionary:
#    print("Yes")
# else:
#    print("No")



# -> 8. You can use the del keyword to remove a specific item, or delete a dictionary. To remove all the dictionary's items, you need to use the clear() method:


# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
#     }
 
# print(len(pol_eng_dictionary)) # outputs: 3
# del pol_eng_dictionary["zamek"] # remove an item
# print(len(pol_eng_dictionary)) # outputs: 2
 
# pol_eng_dictionary.clear() # removes all the items
# print(len(pol_eng_dictionary)) # outputs: 0
 
# del pol_eng_dictionary # removes the dictionary



# 9. To copy a dictionary, use the copy() method:


# pol_eng_dictionary = {
#     "zamek": "castle",
#     "woda": "water",
#     "gleba": "soil"
#     }
 
# copy_dictionary = pol_eng_dictionary.copy()














