#Amorphous data is data which have no specific shape or form – they are just a series of bytes.
#Amorphous data cannot be stored using any of the previously presented means – they are neither strings nor lists.
#There should be a special container able to handle such data.
#Python has more than one such container – one of them is a specialized class name bytearray – as the name suggests, it's an array containing (amorphous) bytes.
#If you want to have such a container, for example, in order to read in a bitmap image and process it in any way, you need to create it explicitly, using one of the available constructors.
#Take a look

data = bytearray(10) 

#Such an invocation creates a bytearray object able to store ten bytes.
#Note: such a constructor fills the whole array with zeros.
#Bytearrays resemble lists in many respects. For example, they are mutable, they're a subject of the len() function, and you can access any of their elements using conventional indexing.
#There is one important limitation – you mustn't set any byte array elements with a value which is not an integer (violating this rule will cause a TypeError exception) and you're not allowed to assign a value that doesn't come from the range 0 to 255 inclusive (unless you want to provoke a ValueError exception).
#You can treat any byte array elements as integer values – just like in the example in the editor:

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))
    
#Now we're going to show you how to write a byte array to a binary file – binary, as we don't want to save its readable representation – we want to write a one-to-one copy of the physical memory content, byte by byte.
#So, how do we write a byte array to a binary file?

from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# # Your code that reads bytes from the stream should go here.
try:
    bf = open('file.bin', 'rb')
    data = bf.read(10)
    bf.close()

    for b in data:
        print(b, end=' ')
    print()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))



#4.3.6 How to read bytes from a stream: 
# Reading from a binary file requires the use of a specialized method name readinto(), as the method doesn't create a new byte array object, but fills a previously created one with the values taken from the binary file.

from os import strerror

data = bytearray(10)

try:
    binary_file = open('file.bin', 'rb')
    binary_file.readinto(data)
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')
        print(bin(b), end=' ')
    print()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# Let's analyze it:

# first, we open the file (the one you created using the previous code) with the mode described as rb;
# then, we read its contents into the byte array named data, of size ten bytes;
# finally, we print the byte array contents – are they the same as you expected?

#An alternative way of reading the contents of a binary file is offered by the method named read().
    
from os import strerror

try:
    binary_file = open('file.bin', 'rb')
    data = bytearray(binary_file.read())
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')
    print()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
    
#Be careful – don't use this kind of read if you're not sure whether the file's contents will fit the available memory.

#If the read() method is invoked with an argument, it specifies the maximum number of bytes to be read.

#The method tries to read the desired number of bytes from the file, and the length of the returned object can be used to determine the number of bytes actually read.
try:
    binary_file = open('file.bin', 'rb')
    data = bytearray(binary_file.read(5))  #Reads 5 bytes only from the file.bin.(Note: the first five bytes of the file have been read by the code – the next five are still waiting to be processed.)     
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')
    print()   #creates new line /Moves the cursor to the next line

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
    

#4.3.7 Copying files - a simple and functional tool
#Now you're going to amalgamate all this new knowledge, add some fresh elements to it, and use it to write a real code which is able to actually copy a file's contents.
from os import strerror

# Buffer for displaying bytes
data = bytearray(10)

# ---- Open source file ----
srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open the source file:", strerror(e.errno))
    exit(e.errno)

# ---- Open destination file ----
dstname = input("Enter the destination file name: ")
try:
    dst = open(dstname, 'wb')
except IOError as e:
    print("Cannot create the destination file:", strerror(e.errno))
    src.close()
    exit(e.errno)

# ---- Copy file using buffer ----
buffer = bytearray(65536)  # 64 KB buffer
total = 0

try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("File copy error:", strerror(e.errno))
    src.close()
    dst.close()
    exit(e.errno)

print(total, "byte(s) successfully written")

src.close()
dst.close()

# ---- Read destination file and print bytes in hex ----
try:
    destData = open(dstname, 'rb')
    data = destData.read(10)

    print("First 10 bytes in destination file:")
    for b in data:
        print(hex(b), end=' ')
    print()

    destData.close()
except IOError as e:    
    print("Cannot read destination file:", strerror(e.errno))     


