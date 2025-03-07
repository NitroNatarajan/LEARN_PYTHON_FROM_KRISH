# print('Hello world')

# import keyword;

# print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
#  'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
#  'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
#    'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


# num1 = int(input('Enter the numerical value you like: \n'))
# num2 = int(input('Enter the second number you like: \n'))

# addition = num1 + num2
# print(f"Addition: {addition}")
# subtract = num1 -num2
# print(f"Subtraction : {subtract}")
# multiply = num1 * num2
# print(f"Multiply : {multiply}")
# division = num1 / num2
# print(type(division))
# print(f"Division : {division}")
# floor_div = num1 // num2
# print(f"floor_div : {floor_div}")
# modulus = num1 % num2
# print(f"modulus : {modulus}")
# exponential = num1 ** num2
# print(f"exponential : {exponential}")

# print("India" == "India")
# a=20
# b=30
# ==  

# print(a == b) # False
# print(a != b) # True
# print(a == 20) #True
# print(a > b) #False
# print(b>a) #True

# conditional statement 
# if -> to execute the task based on the single condition
# if else -> to execute two different action based on the single condition
# is..elif..else..-> to execute the multiple conditional statements 
# nested if -> to check the multiple conditions in a hierarchy..
 
""" number = int(input("Enter a number : \n"))
if number > 0 :
  print(f"This is a positive number : {number}")
  if number%2 == 0:
    print(f"Thus number : {number} is even. ")
  else:
    print(f"The number : {number} is odd")
elif number == 0:
  print(f"The number is neither positive nor negative..")
else:
  print(f"The number : {number} is negative.")
  if number%2 == 0:
    print(f"Thus number : {number} is even. ")
  else:
    print(f"The number : {number} is odd") """


"""
age = int(input("Enter your age : \n"))
if age >= 18:
  print("You are an adult.!!!!")
else:
  print(f"You have to wait {18 - age} years to get an adult badge.")
"""

""" 
num = int(input("Enter the integer : \n"))
if num%2 == 0:
  print(f"This number {num} is even number.")
else:
  print(f"This number {num} is odd number.")
"""

""" word = str(input("Enter the string: "))
if word[0] == 'a' or 'A':
  print('This name is started with {word[0]}') """
""" 
word = input("Enter a string: ")
if 'A' in word or 'a' in word:
  print('This name is started with A') """

# print('Apple'.startswith('A'))

""" age = int(input("Enter the age : "))
if age>= 18:
  print(f"Age {age} , your are eligible to vote.")
else:
  print(f"The age {age}, you will have to wait {18 - age} more years to get voting rights. ") """

""" 
num = float(input("Enter a number: "))
if num > 0:
  print(f"The number: {num} is positive. ")
elif num < 0:
  print(f"The number: {num} is negative. ") 
else:
  print("Zero it is. ")
"""

""" 
mark = float(input("Enter your mark from 0 to 100 : \n"))

if mark>=90:
  print(f"Your mark {mark} is belongs to grade A ")
elif mark>=80:
  print(f"Your mark {mark} is belongs to grade B ")
elif mark>=70:
  print(f"Your mark {mark} is belongs to grade C ")
elif mark>=60:
  print(f"Your mark {mark} is belongs to grade D ")
elif mark>=50:
  print(f"Your mark {mark} is belongs to grade E ")
else: 
  print(f"Your mark {mark} is belongs to grade U. Try your best next time.") 
"""

""" 
day = input("What valid day you were born : ")
if day.lower() == 'saturday'or day.lower() =='sunday' :
  print(f"Your are born on weekend..its {day.upper()} dude..")
else:
  print(f"You are born on weekdays..its {day.upper()}") 
"""

# ternary if else statement 

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# result = a if a>b : "both are same" elif a = b else b

# print(result)


# Loop

# for..loop
# while..loop

# num = 1
# while num<=3:
#   print("Hello")
#   num += 1;

# num = 5
# while num>=1:
#   print(f"Hello: {num}")
#   num -= 1;
""" 
count = 5
while count >= 1:
  print(count)
  count -=1 """
""" 
count = 0
while count < 5:
  print(5- count)
  count += 1; """

""" for num in range(1,11,1):
  print(f"{num} * {5} = {num*5}") 
"""

# for a in "Natarajan":
#   print(a)

# for a in ["Hey", "Hi", "all", "Lets", "Practise", "and", "Rock it"]:
#   print(a)

# for num in range(2,11,2):
#   print(f"Even: {num}")