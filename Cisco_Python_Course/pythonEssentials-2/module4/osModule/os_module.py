#4.4.2 Getting information about the operating system
# Before you create your first directory structure, you'll see how you can get information about the current operating system. This is really easy because the os module provides a function called uname, which returns an object containing the following attributes:

# -> systemname — stores the name of the operating system;
# -> nodename — stores the machine name on the network;
# -> release — stores the operating system release;
# -> version — stores the operating system version;
# -> machine — stores the hardware identifier, e.g., x86_64.

#Example:
import os
print(os.uname())

# The os module allows you to quickly distinguish the operating system using the name attribute, which supports one of the following names:

# -> posix — you'll get this name if you use Unix;
# -> nt — you'll get this name if you use Windows;
# -> java — you'll get this name if your code is written in Jython.
import os
print(os.name)


#4.4.3 Creating directories in Python:The os module provides a function called mkdir, which, like the mkdir command in Unix and Windows, allows you to create a directory.
#The mkdir function requires a path that can be relative or absolute. Let's recall what both paths look like in practice:


# -> my_first_directory — this is a relative path which will create the my_first_directory directory in the current working directory;
# -> ./my_first_directory — this is a relative path that explicitly points to the current working directory. It has the same effect as the path above;
# -> ../my_first_directory — this is a relative path that will create the my_first_directory directory in the parent directory of the current working directory;
# -> /python/my_first_directory — this is the absolute path that will create the my_first_directory directory, which in turn is in the python directory in the root directory.

#Example:
import os

os.mkdir("my_first_directory")   #creates directory in current working directory
print(os.listdir())

import os

os.mkdir("../my_first_directory2")  #creates directory in parent directory of current working directory
print(os.listdir())

# 4.4.4 Recursive directory creation
# The mkdir function is very useful, but what if you need to create another directory in the directory you've just created? Of course, you can go to the created directory and create another directory inside it, but fortunately the os module provides a function called makedirs, which makes this task easier.

# The makedirs function enables recursive directory creation, which means that all directories in the path will be created. Let's look at the code in the editor and see how it is in practice.
#Example:
import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")      #To move between directories, you can use a function called chdir, which changes the current working directory to the specified path
print(os.listdir())
    
# NOTE: The equivalent of the makedirs function on Unix systems is the mkdir command with the -p flag, while in Windows, simply the mkdir command with the path:

# Unix-like systems:
# mkdir -p my_first_directory/my_second_directory
# Windows:
# mkdir my_first_directory/my_second_directory

#4.4.5 Where am I now?
#the os module provides a function that returns information about the current working directory. It's called getcwd.
#Example:
import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.getcwd())
os.chdir("my_second_directory")
print(os.getcwd())
    
#NOTE: On Unix-like systems, the equivalent of the getcwd function is the pwd command, which prints the name of the current working directory.


# 4.4.6 Deleting directories in Python
# The os module also allows you to delete directories. It gives you the option of deleting a single directory or a directory with its subdirectories. To delete a single directory, you can use a function called rmdir, which takes the path as its argument.
#Example1:
import os

os.mkdir("my_first_directory")
print(os.listdir())
os.rmdir("my_first_directory")
print(os.listdir())
    

#Example2:

import os

os.makedirs("dipendra1_directory/dipendra2_directory")
os.chdir("dipendra1_directory")
print(os.listdir())
os.rmdir("dipendra2_directory")
print(os.listdir())

# To remove a directory and its subdirectories, you can use the removedirs function, which requires you to specify a path containing all directories that should be removed:
#Example:
import os

os.makedirs("my_first_directory/my_second_directory")
os.removedirs("my_first_directory/my_second_directory")
print(os.listdir())

#4.4.7 The system() function: All functions presented in this part of the course can be replaced by a function called system, which executes a command passed to it as a string.
#The system function is available in both Windows and Unix. Depending on the system, it returns a different result.
#In Windows, it returns the value returned by the shell after running the command given, while in Unix, it returns the exit status of the process.
#Example:
import os

returned_value = os.system("mkdir my_first_directory")
print(returned_value)

# The above example will work in both Windows and Unix. In our case, we receive exit status 0, which indicates success on Unix systems.
#This means that the my_first_directory directory has been created. As part of the exercise, try to list the contents of the directory where you created the my_first_directory directory.



