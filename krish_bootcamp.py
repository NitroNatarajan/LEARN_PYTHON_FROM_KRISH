# Lets start with python basic to advanced with DSA 
# single line comment

""" 
Multi line comment  
"""
# Basic syntax rules in the python 
# case sensitivity 
  # Indentation - to define the block of code ({ } used in the other language for this purpose ) or 
  # define the structure and hierarchy of the code - consistent use of 4 space or tab
# Indentation to determine the grouping of statements.
# Indentation to define the blocks in the conditional and looping statements 
age = 32;
if age>30:
  print('age: ', age);

# Line continuation - use backlash \: 
sum = 1+2+1+\
9+8+7+1;
print(sum)

# Multiple statements on a single line, the statements are separated by the colon ";" 
sum = 12; sub = 90; mul = 56; divi = 23
print(divi)

# understanding semantics 
# Variable assignment
age =32
name = 'Nitro'
is_major = True

# no data type specification required while declaration and assigning,so its called dynamically typed. 
# During the runtime, the kernel understand its type through the values assigned to the variable.

# name = 'Nitro' -> str type -> string type which is quoted -> letter and number, symbol, any word, any 
# combined characters wrapped with the quoted are string.

# we can change the data type of variable from one to another through the values belongs to specific data type. 
# During the runtime, those values are evaluated. 
# Thats called type inference which means the data type of the variable get automatically conceived and 
# converted to the value type set to the variable. 

# type checking
# print(type(name)) -> <class 'str'>
# print(type(age)) -> <class int>
# print(type(4.25)) -> <class float> 
# print(type(True)) -> <class bool>

# These are the primitive data types in the python.

# error : 
  # 1. Indentation error
  # 2. Name Error : name 'b' is undefined when a = b; while b is not defined before.
  #    we will see the how to handle these error later.

# word = int(input("Enter the word: "))
# for letter in word:
#   if letter == 'o':
#     continue
#   print(letter)

# while checking the list items in the list, if they found the particular item, 
# it can end up the loop or it can continue that particular list item.

str1 = 'Python';str2 = 'Programming'
print(str1," ",str2)
print(str1[1])

str12 = 'Python Programming'
str12.split(" ")