# Python Learning through *Krish Naik* Course

>>The more and more practise code examples in the notebook.ipynb file in the same repository.
## Getting started with VS Code
  - Git integrated 
  - CLI interaction
  - Environment development - to manage the python packages for the python project..
  - To create the environment we use the conda command > conda create -p venv python == 3.13.0 
  - To activate the environment we must need to activate it by > conda activate venv/ 
  - lets work on our learning about the basic syntax and semantics
## Python Basics - Syntax and Semantics 
  - Single and multi - line comment
  - Definition of syntax and semantics
  - Basic syntax rules in Python
  - Understanding the semantics in Python
  - Common syntax errors and How to avoid them.
  - practical code examples 
  - Indentation - to define the block of code 
  - Line continuation
### Comment: 
  - Comment is a notes that developers write in the code file to manifest what it really means to do for the others to understand the code easily. 
  - There are two types of comments we can use in the python. Single line comment and Multi line comment. 
  - Single line comment # Single line comment.
  - Multi line comment '''Multiline comment'''.
### Syntax:
  Syntax refers to the set of rules that defines the combination of symbols that are considered to be correctly structure the programs in a language. 
  In short, syntax is about the correct arrangement of words and symbols in a code. 
  - If we don't follow the right syntax, we will end up with errors. 
### Semantics:
  - Semantics refers to the meaning or interpretation of the symbols, characters and commands in a language.It is about what the code is supposed to do when it runs.
### Indentation:
Indentation in python is used to define the structure and hierarchy of the code. wkt, Javascript and other lang uses the braces {} uses this to define the blocks. 
But in python we use the indentation for this structuring or to determine the grouping of the statements. This means that all the statements within the block are indented at the same level. 
### Type Inference
Type inference is a compiler's ability to automatically determine the type of a variable, function, or expression in a program. It's based on the program's structure and context. 
### How it works 
- Type inference can be done at compile time or runtime.
- It can be used to assign types to variables, constants, and functions.
- It can help detect type rule violations and report them during compilation.
### Common Errors: 
 - Syntax error 
 - Name error
 - Indentation Error

## Variables 

Variables are fundamental elements in the programming language used to store the data that can be referenced and manipulated in a program as per our needs. 
In python, variables are created when we assign the value to them, and they do not need an explicit declaration to reserve memory space. The declaration happen automatically when we assign the values to the variable. 

### Things we gonna see in this section: 
- Introduction to the variable
- Declaration and Assigning variables
- Naming conventions
- Understanding variable types
- Type checking and conversion 
- Dynamic typing 
- Practical examples and errors possibility while work with variable

### Naming convention for the variable while defining 
Rules and Best practices: 
  - No variable should start with symbols and number or symbols or reserved operator such as + - * & $, except _. It can start with the _ for separate the word if the variable contains multiple words. 
  - Variables names are descriptive in nature for the code readability.
  - Variable names are case sensitive.

## Data Types:
### Definition: 
- Data types are the classification of data which tell the compiler or interpreter how the programmer intend to use the data 
- They determine the type of operations that can be performed on the data, the values that the data can take and the amount of memory needed to store the data. 
### Importance of Data types in the Programming Languages:
- Data types ensures the data is stored in an efficient way
- They help in performing correct operation on data
- Proper use of data types prevent us from the bugs and errors in the program.
### Basic Data Types 
- Integer
- Floating-point number
- Strings
- Boolean
### Advanced Data Types
- Lists
- Tuples
- Sets
- Dictionaries

## Deep dive into the Operation/operator's In Python 
### Introduction to Operators
### 1. Arithmetic Operators
- Addition
- Subtraction
- Multiplication
- Division
- Floor division
- Modulus
- Exponentiation 

### 2. Comparision Operators
- Double Equal to check == (equality check) 
- Not equal to != 
- Greater than > 
- Greater than or equal to >=
- Lesser than < 
- Lesser than or equal to <= 

### 3. Logical Operator
- AND
- OR
- NOT
**Truth table for AND , OR**
   
| P	| Q	| AND | OR  | 
|---|---|-----|-----|
| T	| T |	T   |	 T  |	
| T	| F	| F	  |  T	|
| F	| T |	F  	|  T	|
| F	| F |	F   |	 F  |

**Truth table for NOT**
| P | NOT |
|---|-----|
| T | F   |
| F | T   |

### 4. Assignment Operator
 =, +=,-=,*=,/=, **=, //=, %=, &=, !=, ^=, >>=, <<=, := 

### 5. Identity Operators
- is 
- is not 

### 6. Membership operator 
- in 
- not in 

### 7. Bitwise operator
- &     ========= Bitwise AND
- |     ========= Bitwise OR
- ^     ========= Bitwise NOR
- ~     ========= Bitwise NOT
- <<    ========= Left shift operator
- \>\>  ========= Right shift operator

Operators: 
  For any operations like arithmetic, logical, assigning operations we do with the data of any format, we need an operators to calculate or determine the output by processing it with the operators 
  like we do in the mathematics using the + - * % / etc..Here we will see all the available operators and its use cases in the below code. 
