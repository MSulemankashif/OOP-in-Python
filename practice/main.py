# Building a Mini Calculator

a = int(input("Enter a first value: "))
b = int(input("Enter a second value: "))
op = input("Enter an Operator (+, -, *, /, %, **): ")

if(op == "+"):
    print(a + b)
elif(op == "-"):
    print(a - b)
elif(op == "*"):
    print(a * b)
elif(op == "/"):
    print(a / b)
elif(op == "%"):
    print(a % b)
elif(op == "**"):
    print(a ** b)
else:
    print("Invalid Operation")