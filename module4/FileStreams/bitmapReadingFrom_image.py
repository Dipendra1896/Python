# We are  going to process a bitmap stored in a file named image.jpg, and you want to read its contents as a whole into a bytearray variable named image. 

try:
    stream = open("image.jpg", "rb")
    image = bytearray(stream.read())
    print("Image data:")
    print(image)
    stream.close()
except IOError:
    print("failed")
else:
    print("success")