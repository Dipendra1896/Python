try:
    stream = open("/home/dipendra/Documents/python/Cisco_Python_Course/pythonEssentials-2/module3/dipendra.txt","rt")
    #processing
    print(stream.read())
    stream.close()
except Exception as exc:
    print("Can not open the file", exc)


import errno

try:
    s = open("/home/dipendra/Documents/python/Cisco_Python_Course/pythonEssentials-2/module3/dipendra.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)
        


# Fortunately, there is a function that can dramatically simplify the error handling code.

# Its name is strerror(), and it comes from the os module and expects just one argument – an error number.

# Its role is simple: you give an error number and get a string describing the meaning of the error.

from os import strerror

try:
    #s = open("c:/users/user/Desktop/file.txt", "rt")
    s = open("/home/dipendra/Documents/python/Cisco_Python_Course/pythonEssentials-2/module3/dipendra.txt", "rt" ,encoding = "utf-8")
    # Actual processing goes here.
    print(s.read())
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))
    

#4.3 Section 3 – Working with real files:
#4.3.1 Processing text files
from os import strerror

try:
    counter = 0
    stream = open('text.txt', "rt")
    char = stream.read(1)
    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\n\nCharacters in file:", counter)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
    


from os import strerror

try:
    counter = 0
    stream = open('text.txt', "rt")
    content = stream.read()
    for char in content:
        print(char, end='')
        counter += 1
    stream.close()
    print("\n\nCharacters in file:", counter)
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))
    


#4.3.2 readline():If you want to treat the file's contents as a set of lines, not a bunch of characters, the readline() method will help you with that.The method tries to read a complete line of text from the file, and returns it as a string in the case of success. Otherwise, it returns an empty string.

from os import strerror

try:
    character_counter = line_counter = 0
    stream = open('text.txt', 'rt')
    line = stream.readline()
    while line != '':
        line_counter += 1
        for char in line:
            print(char, end='')
            character_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCharacters in file:", character_counter)
    print("Lines in file:     ", line_counter)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
    
#4.3.3 readlines():It treats text file as a set of lines, not characters, is readlines().The readlines() method, when invoked without arguments, tries to read all the file contents, and returns a list of strings, one element per file line.

stream = open("text.txt")
print(stream.readlines(20))    #The maximum accepted input buffer size is passed to the method as its argument.
print(stream.readlines(20))
print(stream.readlines(10))
stream.close()

# #Note: when there is nothing to read from the file, the method returns an empty list. Use it to detect the end of the file.readlines(n) does not read n lines — it reads up to n bytes

from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
    
#There are two nested loops in the code: the outer one uses readlines()'s result to iterate through it, while the inner one prints the lines character by character.


#4.3.4 Dealing with text files: write()
# Writing text files seems to be simpler, as in fact there is one method that can be used to perform such a task.The method is named write() and it expects just one argument – a string that will be transferred to an open file (don't forget – open mode should reflect the way in which the data is transferred – writing a file opened in read mode won't succeed).
#Example:

from os import strerror

try:
	file = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.The open mode 'w' ensures that the file will be created from scratch
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
	file.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
    
# Can be also written as:
from os import strerror

try:
    file = open('newtext1.txt', 'wt')
    for i in range(10):
        file.write("line #" + str(i+1) + "\n")
    file.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
    


    
import sys
sys.stderr.write("Error message \n")

