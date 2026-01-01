number1 = int (input("Enter first number: "))
number2 = int (input("Enter second number: "))
number3 = int (input("Enter second number: "))
if number1 > number2:
    largestNumber = number1
elif number2 > number3:
    largestNumber = number2
else:
    largestNumber = number3
print("The largest number is:", largestNumber)