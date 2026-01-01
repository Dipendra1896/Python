# empty_tuple = ()
# print(type(empty_tuple))

# one_elem_tuple_1 = ("one", )    # Brackets and a comma.
# one_elem_tuple_2 = "one",       # No brackets, just a comma.

# print(one_elem_tuple_1)
# print(one_elem_tuple_2)

# my_tuple_1 = 1, 
# print(type(my_tuple_1))    # outputs: <class 'tuple'>

# my_tuple_2 = 1             # This is not a tuple.
# print(type(my_tuple_2))    # outputs: <class 'int'>

# # we can print tuple by indexing them
# my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
# print(my_tuple[3])    # outputs: [3, 4]
# print(my_tuple[2])    # outputs: string
# print(my_tuple[5])    # outputs: True
# print(my_tuple[4])    # outputs: (5, )


# 6. You can loop through a tuple elements (Example 1), check if a specific element is (not)present in a tuple (Example 2), use the len() function to check how many elements there are in a tuple (Example 3), or even join/multiply tuples (Example 4):

# tuple_1 = (1, 2, 3)
# for elem in tuple_1:
#     print(elem)
# print(5 in tuple_1) 
# print(5 not in tuple_1)
# print(len(tuple_1))

# tuple_2 = (4, 5, 6)
# tuple_3 = tuple_1 + tuple_2
# tuple_4 = tuple_1 *2

# print(tuple_2)
# print(tuple_3)
# print(tuple_4)


# You can also create a tuple using a Python built-in function called tuple(). This is particularly useful when you want to convert a certain iterable (e.g., a list, range, string, etc.) to a tuple:
# my_tuple = tuple((1, 2, 3, "string"))
# print(my_tuple)

# my_list = [4, 5, 6]
# print(my_list)     #outputs: [4, 5, 6]
# print(type(my_list))  #outputs: <class 'list'>
# tup = tuple(my_list)
# print(tup)          #outputs: (4, 5, 6)
# print(type(tup))    #: <class 'tuple'>

# # tuple to list conversion
# tuple = (1,2,3)
# my_list = list(tuple)
# print(my_list)
# print(type(my_list))




# 1. Dictionaries are unordered*, changeable (mutable), and indexed collections of data. (*Since Python 3.6x dictionaries have become ordered by default.Each dictionary is a set of key: value pairs. You can create it by using the following syntax:

# my_dictionary = {
#     key1:value1,
#     key2:value2,
#     key3:value3
# }

# 2. If you want to access a dictionary item, you can do so by making a reference to its key inside a pair of square brackets (ex. 1) or by using the get() method (ex. 2):

# my_dict = {
    # "name1":"Dipendra",
    # "name2":"Rajat",
    # "name3":"sanoj"
# }

# item1 = my_dict["name3"]  #ex.1
# print(item1)
# item2 = my_dict.get("name2") #ex.2
# print(item2)


#3. If you want to change the value associated with a specific key, you can do so by referring to the item's key name in the following way:

# pol_eng_dictionary = {
    # "name1":"Dipendra",
    # "name2":"Rajat",
    # "name3":"sanoj"
#     }

# pol_eng_dictionary["name3"] = "Sujan"
# item = pol_eng_dictionary["name3"]
# print(item)  # outputs: Sujan

# 4. To add or remove a key (and the associated value), use the following syntax:

# my_dict = {}
# my_dict["name1"] = "Dipendra"  # add a key-value pair
# print(my_dict)  #outputs: 'name1':'Dipendra'
# del my_dict["name1"]  #delete key-value pair
# print(my_dict)


# You can also insert an item into a dictionary by using the update() method, and remove the last element by using the popitem() method, e.g.:

# pol_eng_dictionary = {"kwiat": "flower"}

# pol_eng_dictionary.update({"gleba": "soil"})
# print(pol_eng_dictionary)    # outputs: {'kwiat': 'flower', 'gleba': 'soil'}

# pol_eng_dictionary.popitem()
# print(pol_eng_dictionary)    # outputs: {'kwiat': 'flower'}

#5. You can use the for loop to loop through a dictionary, e.g.:
# pol_eng_dictionary = {
#     "name1":"Dipendra",
#     "name2":"Rajat",
#     "name3":"sanoj" 
#     }

# for item in pol_eng_dictionary:
#     print(item)


#6. If you want to loop through a dictionary's keys and values, you can use the items() method, e.g.:
# pol_eng_dictionary = {
    # "name1":"Dipendra",
    # "name2":"Rajat",
    # "name3":"sanoj" 
#     }

# for key, value in pol_eng_dictionary.items():
#     print("name/value ->", key, ":" , value)

#7. To check if a given key exists in a dictionary, you can use the in keyword:
# pol_eng_dictionary = {
#    "name1":"Dipendra",
#     "name2":"Rajat",
#     "name3":"sanoj" 
    
#     }

# if "name1" in pol_eng_dictionary:
#    print("Yes")
# else:
#    print("No") 




