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

# # Print all odd numbers from 0 to 10

# for i in range(2, 11, 2):
#     print(i)

# Print all Even numbers from 0 to 10

for i in range(1, 11, 2):
    print(i)

    # Print all odd numbers from 1 to 20

for i in range(2, 21, 2):
    print(i)

    # Print the table of 57

for i in range(1, 11):
    print(57, "x", i, "=", 57*i)

# Print all multiples of 3 from 1 to 50 but skip 15

for i in range(1, 51):
    if( i % 3 == 0):
        print(i)

    if(i == 15):
        continue


# Take two integers a and b as input
# Find and print the first number between 1 and 1000 that is divisible by both numbers

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

num = range(1, 1001)

for i in num:
    if(a % i == 0 and b % i == 0):
        print(i)

        # List in Python

marks = [29,56,74,39,78]
# List Methods

print(len(marks))
print(marks[-1])

# Slicing

print(marks[0:3])
print(marks[-3:])

marks = [45,67,89,54,44]

marks.insert(0, 50)

print(marks)

# Non Primtive Data types
# List, Tuple, Set, Dictionary

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

# # Print all odd numbers from 0 to 10

# for i in range(2, 11, 2):
#     print(i)

# Print all Even numbers from 0 to 10

for i in range(1, 11, 2):
    print(i)

    # Print all odd numbers from 1 to 20

for i in range(2, 21, 2):
    print(i)

    # Print the table of 57

for i in range(1, 11):
    print(57, "x", i, "=", 57*i)

# Print all multiples of 3 from 1 to 50 but skip 15

for i in range(1, 51):
    if( i % 3 == 0):
        print(i)

    if(i == 15):
        continue


# Take two integers a and b as input
# Find and print the first number between 1 and 1000 that is divisible by both numbers

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

num = range(1, 1001)

for i in num:
    if(a % i == 0 and b % i == 0):
        print(i)

        # List in Python

marks = [29,56,74,39,78]
# List Methods

print(len(marks))
print(marks[-1])

# Slicing

print(marks[0:3])
print(marks[-3:])

marks = [45,67,89,54,44]

marks.insert(0, 50)

print(marks)

# Non Primtive Data types
# List, Tuple, Set, Dictionary

# Dictionary

marks = {
    "maths": 97,
    "physics": 89,
    "chemistry": 77 
}

for key in marks:{
    print( marks[key])
}

# Given a List of Roll Numbers: [101, 105, 102, 101, 108, 105, 110]. Print all unique roll numbers in the list

roll = {101, 105, 102, 101, 108, 105, 110}

print(roll)

# Given Employee Records in the form of a list of tuples where each tuple contains:
# (Employee Id, Employee Name, Salary)


data = [
    (101, "Ali", 50000),
    (102, "Ahmed", 45000),
    (102, "Aslam", 70000)
]

emp_id = int(input("Enter Employee Id to see it's record: "))

found = False

for employee in data:
    if employee[0] == emp_id:
        print("\n Employee Record Found")
        print("Employee id =", employee[0])
        print("Employee Name =", employee[1])
        print("Employee Salary =", employee[2])

        found = True

if not found:
     print("Employee Record not Found")


     # Modules

# from math import sqrt

# print(sqrt(16))

import random

print(random.randint(1,7))

# Check weather a number is a even or odd number

def check_number(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

number = int(input("Enter a number to check weather it's Odd or Even: "))

check_number(number)


# Write a function to count vowels in a string

def count_char(text):
    count = 0

    for char in text.lower():
        if char in "aeiou":
            count += 1

    print("Total vowels", count)

text_in = input("Enter text here: ")

count_char(text_in)

# Write a function to check weather a number is prime or not

def check_prime(num):

    if num <= 1:
        print("Not Prime")
        return

    for i in range(2, num):

        if num % i == 0:
            print("Not Prime")
            return

    print("Prime Number")

number = int(input("Enter a number here: "))

check_prime(number)


# Write a function that returns a average marks if a list of marks is passed as a parameter

def average_func(marks):

    total = sum(marks)

    average = total / len(marks)
    return  average

student_marks = [80, 70, 90, 60]

result = average_func(student_marks)

print("Average Marks: ", int(result))



import random

def play_game():

    lucky_num = random.randint(1, 50)

    while True:
        user_input = int(input("Guess the Lucky Number: "))

        if user_input == lucky_num:
            print("You Won The Game!!!")
            break

        elif(user_input < lucky_num):
            print("Less than Lucky Number. Try Again")
        else:
            print("Greater than Lucky Number. Try Again")

play_game()


# List Methods

my_list = [1,3,4,5,2,7,6]

my_list.append(9)
# my_list.sort()
my_list.sort(reverse=True)
my_list.reverse()
my_list.insert(-1, 8)

print(my_list)


# Tuple Methods

tup = (1,3,2,4,5, 1)

tup.index(5) #Returns index of First Occurence
tup.count(1) #Returns total occurences of element
print(tup) 

# WAP to ask the user to enter names of their 3 favorite movies and store them in a list

mov1 = input("Enter first movie name here: ")
mov2 = input("Enter second movie name here: ")
mov3 = input("Enter third movie name here: ")

list = [mov1, mov2, mov3]

print(list)
print(type(list))


# WAP to check if a list contains a palindrome of elements 

myList = ["r", "a", "c", "e", "c" ,"a", "f"]

myList_copy = myList.copy()
myList_copy.reverse()

if myList_copy == myList:
    print("Palindrome")
else:
    print("Not Palindrome")
