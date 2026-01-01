# numbers = [10, 20, 30, 40, 50, 60.0]
# print(numbers[1])
# print(max(numbers))
# print(numbers[4])

# numbers = [10, 5, 7, 2, 1]
# print("Original list contents:", numbers)  # Printing original list contents.

# numbers[0] = 111
# print("New list contents: ", numbers)  # Current list contents.

# numbers = [10, 5, 7, 2, 1]
# print("Original list contents:", numbers)  # Printing original list contents.

# numbers[0] = 111
# print("\nPrevious list contents:", numbers)  # Printing previous list contents.
# # swapping first element with fourth element
# x = numbers[4] 
# numbers[4] = numbers[1] 
# numbers[1] = x
# print("Latest list contents:", numbers)
# del numbers[1]
# numbers[1] = 20
# print(len(numbers))
# print(numbers)

# append() and insert() function
# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)

# numbers.append(4)  #insert new element at the last 
# print(len(numbers))
# print(numbers) 

# numbers.insert(0, 222) #insert 222 at index 0
# print(len(numbers))
# print(numbers)
# numbers.insert(1, 333)
# print(numbers)
# print(len(numbers))


# my_list = []  # Creating an empty list.
# for i in range(5):
#     my_list.append(i + 1)
# print(my_list)

# my_list = []  # Creating an empty list.
 
# for i in range(5):
#     my_list.insert(0, i + 1)
 
# print(my_list)

# my_list = [2,3,4]
# your_list = [2,3,4]
# for i in range(4,14):
#     my_list.append(i+1)
# print(my_list)

# for i in range(4,14):
#     your_list.insert(0,i+1)
# print(your_list)


# my_list = [10, 1, 8, 3, 5, 3]
# total = 0
# for i in my_list:
#     total += i
# print(total)

# step 1
beatles = []

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# step 3
for member in ["Stu Sutcliffe", "Pete Best"]:
    name = input(f"Add {member} to the band: ")
    beatles.append(name)

# step 4
# del beatles[3]
# del beatles[3]

# step 5
beatles.insert(0, "Ringo Starr")

print("The Beatles:", beatles)
