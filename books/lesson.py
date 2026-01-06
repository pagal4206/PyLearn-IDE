lessons = {
    "Print": '''print("PyLearn IDE")

#variable
variablen_name= 1
print(variablen_name)
''',

    "Data Types" : '''# integer

var1 = 10   #  int
print(type(var1))

# float

var1 = 10.5   #  float
print(type(var1))

# boolean

var1 = True  #  bool
print(type(var1))

# string

var1 = "PyLearn IDE"   #  str
print(type(var1))

# list 

var1 = [10, 20, 30, "PyLearn IDE", 20.3]   #  list
print(type(var1))

# tuple 

var1 = (10, 20, 30, "PyLearn IDE", 20.3)   #  tuple
print(type(var1))

# set 

var1 = {10, 20, 30, "PyLearn IDE", 20.3}  #  set
print(type(var1))

# dictionary 

var1 = {"name": "Dilip Choudhary", "age": 21}   #  dict
print(type(var1))
''',

    "Assigning Variable" : '''#==================Assigning Multiple value==================
x, y, z= 5, 5.2, "PyLearn IDE"

#==================Assigning  Same Value Multiple Variable==================

x=y=z="PyLearn IDE"

#==================Re Assigning Variable==================

x=45
print(x)
x="PyLearn IDE" #Re Assinging
print(x)
''',

    "Python Operator" : '''#Arthmetic operator       +,-,*,/,%,**,//

#   +  addition
var1 = 12
var2 = 45
result = var1 + var2
print(result)

#   - Subtraction

var1 = 12
var2 = 45
result = var1 - var2
print(result)


#   *  Multiplication

var1 = 12
var2 = 45
result = var1 * var2
print(result)

#   / Division

var1 = 12
var2 = 45
result = var1 / var2
print(result)

#   %  Modulus

var1 = 12
var2 = 45
result = var1 % var2
print(result)

#   ** Exponentiation

var1 = 12
var2 = 45
result = var1 ** var2
print(result)

#   //  Floor Division

var1 = 12
var2 = 45
result = var1 // var2
print(result)


#Assignment Operators    =,+=,-=,*=,/=,%=,**=,//=

#  =  Assigns

var1 = 12
result = var1
print(result)

#   += Add Assign

var1 = 12
var1 += 2
result = var1
print(result)

#   -= Subtract Assign

var1 = 12
var1 -= 2
result = var1
print(result)

#  *= Multiply Assign

var1 = 12
var1 *= 2
result = var1
print(result)

#  /= Divide Assign

var1 = 12
var1 /= 2
result = var1
print(result)

#  %=  Modulus Assign

var1 = 12
var1 %= 2
result = var1
print(result)

#  **= Exponent Assign

var1 = 12
var1 **= 2
result = var1
print(result)

#  //= Floor Division Assign

var1 = 12
var1 //= 2
result = var1
print(result)


# Comparison Operator  ==,!=,>,<,>=,<=

# == Equal Both

var1 = 12
var2 = 12
result = var1 == var2
print(result)

#  !=  Not Equal

var1 = 12
var1 = 45
result = var1 != var2
print(result)

# >  Greater Than

var1 = 12
var1 = 45
result = var1 > var2
print(result)

# < Less Than

var1 = 12
var1 = 45
result = var1 < var2
print(result)

#  >= Greater Than Or Equal

var1 = 12
var2 = 45
result = var1 >= var2
print(result)

# <= Less Than Or Equal

var1 = 12
var2 = 45
result = var1 <= var2
print(result)

# Logical Operators  &&(AND), || (OR), ! (NOT)

#  && (AND) And Operator

var1 = 12
var2 = 45
result = var1 > 5 and var2 > 30  # Both Condition Are True
print(result)

#  || (OR)

var1 = 12
var2 = 45
result = var1 > 5 or var2 < 30   #  One Condition Are True
print(result)

# !(NOT)

var1 = 12
print(not var1 > 5)   # not  True  =   False
print(not var1 < 5)  # not  False =   True


#  Identity Operator    is, is not

#   is  Operator

var1 = 12
var2 = var1
result = var1 is var2
print(result)

#   is not  Operator

var1 = 12
var2 = var1
result = var1 is not var2
print(result)

# Membership Operator  in, not in

#  in operator

var1 = "ram", "ramesh", "suresh", "Dilip Choudhary"
result = "ramesh" in var1
print(result)

#  not in operator

var1 = "ram", "ramesh", "suresh", "Dilip Choudhary"
result = "ramesh" not in var1
print(result)

''',

    "IF-ELIF-ELSE" : '''# Types  if,  if-else,  nested if,  if-elif-else


#  if

var1 = 12
if (var1 > 10) :
    print("var1 is greater than 10")

#  if-else

var1 = 12
if (var1 < 10) :
    print("var1 is greater than 10")
else:
    print("var1 is not less than 10")

#  nested if

var1 = 12
if (var1 > 10) :
    print("var1 is greater than 10")
    if (var1 == 10) :
        print("var1 is Equal to 10")
    else:
        print("var1 is greater, but not equal to 10")
else:
    print("var1 is not greater than 10")

#  if-elif-else

var1 = 12
if (var1 > 10) :
    print("var1 is greater than 10")
elif (var1 < 10) :
    print("var1 is less than 10")
else:
    print("var1 is equal to 10")

''',

    "Loops" : '''#  while loop

var1 = 1
while var1 <= 5:
    print(var1)
    var1 += 1

#  for loop
var1 = 1
for var1 in range(5):
    print(var1)

#   list, tuple, string

# list

var1 = ["45", "65", "64"]
print(var1[1])

for lo in var1:
    print(lo)   # loop

# tuple

var1 = ("45", "65", "64")
print(var1[2])

for lo in var1:
    print(lo)  # loop

# string

var1 = "PyLearn IDE"
print(var1[2])

for lo in var1:
    print(lo)  # loop

    
#==================range(start,stop,step)==============


# range

for lo in range(5):
    print(lo)

# start and stop

for lo in range(1, 7):
    print(lo)

# start stop step

for lo in range(1, 7, 2):
    print(lo)

#==================break continue==============

# break

var1 = 1
while var1 <= 10:
    print(var1, end="")
    if (var1 == 5) :
        break
    var1 += 1
print("Done")

# continue

var1 = 1
while var1 < 10:
    var1 += 1
    if var1 == 5:
        continue
    print(var1)
    
''',
    "Functions" : '''# define function

def dilip():
    print("Hello Everyone")
dilip()

# define+return function
def dilip():
    return "Hello Everyone"
print(dilip())

# example

def calc(a=10, b=10):
    return a+b
print(calc())

''',
    "Classes & Objects" : '''# class & obj

class dilip:
    def __init__(self, name, age):
        self.name = name 
        self.age = age          # public exp.. self.age = age
    def show(self):
        print(f"My Name Is {self.name}")
        print(f"I Am {self.age} Years Old")
        
# objects

var1 = dilip("Dilip Choudhary", 21)
var1.show()


# class & obj 

class dilip:
    def __init__(self, name, age):
        self.__name = name 
        self.__age = age          #   privet  exp... self.__age = age
    def __show(self):
        print(f"My Name Is {self.__name}")
        print(f"I Am {self.__age} Years Old")
        
# objects

var1 = dilip("Dilip Choudhary", 21)
var1._dilip__show()

''',

    "File Handling" : '''# File Creat And Write

file = open("dilip.txt", "w")   
file.write("Hello dilip")   
file.close()   
print("File Created")   

# File Read

file = open("dilip.txt", "r")  
print(file.read())  
file.close()   

# File Append (file ke andar last me line add kerna)

file = open("dilip.txt", "a")   
file.write("I Am Fine Now You Say...")  
file.close()   
print("Line Append")  

# File Read (dobara read kiya check ke liye ki last append ya line add hua ki nai)

file = open("dilip.txt", "r")   
print(file.read())  
file.close()  

# File Rename

import os   
if os.path.exists("dilip.txt"):  
    os.rename("dilip.txt", "Dilip.txt")
    print("File Rename")  
else:
    print("File Not Found")  

# File Delete

import os      
if os.path.exists("Dilip.txt"): 
    os.remove("Dilip.txt")   
    print("File Deleted") 
else:
    print("File Not Found")  
'''
}