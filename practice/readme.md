# age = input("Enter your age: ")

# This is called type casting bcz we are changing it's type
# new_age = int(age) + 1

# print (1 + 1.25) # implicit
# print (1 + int(2.9999)) #explicit

a = int(input("Enter a number A: "))
b = int(input("Enter a number B: "))

sum = a+b

print("Sum: " , sum)




# String Operations

name = "Tony Stark"

# print(name.upper()) # Convert to uppercase
# print(name.lower()) # Convert to Lowercase
# Strings are Immutable, so we cannot change the original string directly. Instead, we can create a new string with the desired changes.

# print(name.find("ark"))
print(name.replace("Tony Stark", "Iron Man"))
print(name)

# Check for Presence
name = "Muhammad Suleman"

print('Suleman' in name)

# Reserved Keywords in Python
# True, in, False, break, continue, return, for

# Practice Exercise

# Take price of 3 products as input
# print the total
# print the average price

input1 = int(input("Enter a first product price: "))
input2 = int(input("Enter a second product price: "))
input3 = int(input("Enter a third product price: "))

sum = input1 + input2  + input3

avg = (input1 + input2  + input3 / sum)

print(sum)
print(avg)

# Take a superhero name as input and check if it starts with 'S' / 's' or not

name = input("Enter your name here: ")

print(name.startswith("S"))

# print(10 % 3)  Modulo Operator ->remainder

print( 6 ** 2)

# Operator Precedence

ans = (2 + 5) * 3
print(ans)

# THis is called Operator Precedence

print(3 > 5 or 5> 3) #Dono me sy ek value true hogi tsb true return kary ga

print(6> 7 and 8 > 5) #Dono values true honi chahiye tab hi true return hoga

print(not 3 > 2) # True ka answer false and False ka answer true

Total_marks = 550
Obt_marks = 350

percentage = Obt_marks / Total_marks * 100

if(percentage >= 80):
    print("Congrats! Your Grade is A+")
elif(percentage >= 60):
    print("Your Grade is B")
elif(percentage >= 50):
    print("Your Grade is C")
else:
    print("Fail")

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

 <!-- WHile Loop -->
 i = 5

while i >= 0:
    print(i * "hello")
    i  -= 1

print("end of code")

# Odd Numbers
for  i in range(2, 11, 2):
    print(i)


num = int(input("Enter a number for it's table: "))

for i in range(1,11):
    res = num * i
    print(num , "x" , i , "=" , res)

    if res == 21:
        break
    else:
        continue