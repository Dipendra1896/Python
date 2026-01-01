# my_list = [8, 10, 6, 2, 4,12, 1, 3, 5, 2]  # list to sort
# swapped = True  # It's a little fake, we need it to enter the while loop.

# while swapped:
#     swapped = False  # no swaps so far
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # a swap occurred!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print(my_list)


# my_list = []
# swapped = True
# num = int(input("How many elements do you want to sort: "))

# for i in range(num):
#     val = float(input("Enter a list element: "))
#     my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print("\nSorted:")
# print(my_list)

# my_list = [8, 10, 6, 2, 4]
# my_list.sort()
# print(my_list)


#Using sort() method for sorting the list
# my_list = []
# num = int(input("How many elements do you want to sort: "))
# for i in range(num):
#     val = float(input("Enter a list element: "))
#     my_list.append(val)

# my_list.sort()
# print(my_list)

# using reverse() method
lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()
print(lst)  # outputs: [4, 2, 1, 3, 5]

