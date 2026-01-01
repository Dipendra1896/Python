for line in open("sampleFile.txt", "rt"):
    print(line, end='')

#The code copies the file's contents to the console, line by line. Note: the stream closes itself automatically when it reaches the end of the file.