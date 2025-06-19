#Making a simple calculator! OwO

#Introduction
print("Welcome to my Simple Calculator!")
number = float(input("Select the first NUMBER for the operation: "))
number2 = float(input("Select another NUMBER to proceed: ")) #"Float" is allowing the user to input decimals

#Step 1, Operation
print("1. Add them!")
print("2. Subtract them!")
print("3. Multiply them!")
print("4. Divide them!")

#Step 2, Ifs statement and confirming user input
operation = int(input("Great! Select one of these operations to apply to your NUMBERS: "))
if operation == 1:
    result1 = (number + number2)
elif operation == 2:
    result1 = (number - number2)
elif operation == 3:
    result1 = (number * number2)
elif operation == 4:
    if number2 !=0:    
        result1 = (number / number2)
    else:
        result1 = print("Invalid 2nd number, can't divide by zero!")
else:
    result1 = print("Invalid input. Restart Program.")

#Final result
print("So, the result would be: " + str(result1))