"""
first_day.py - Display Hello World
Created by Sok Den - 25th/12/2020
Note:
1. (cd) command to navigate to the day_two folder
2. (dir) or (ls) command to make sure hello_world.py is in this folder
3. (python hello_world.py) command run the file
4. (cls) for clear screen
"""
# Display hello world
print("Hello World")

# Display enter line
print("hello\nworld")

# Display quatation mark
print("hello\"world")

# Display plus string
character_name = "Sok Den"
character_age = "20"
print("Your name is: " + character_name + " , and your age is: " + character_age)

# Dispaly font lower and upper
phrase = "Den Gamedev"
print(phrase.lower())
print(phrase.upper())

# Display true or false
phrase_two = "a b c"
print(phrase_two.islower())
print(phrase_two.isupper())

print(phrase_two.lower().islower())
print(phrase_two.upper().isupper())

# Display រាប់អក្សរ
print(len(phrase))

# Dispaly character
print(phrase[0])

# Display number
print(phrase.index("G"))

# Display replace character
print(phrase.replace("Den", "@sokden"))

# Display number
print(2020)

# Display calculate
print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2)
print(1 % 2)

print(1 - 2 * (2))

# Convert to string
my_num = 5
print(my_num) # This is int
print(str(my_num)) # Converted to string

# print(my_num + " My favorite number") # Error, int + str
print(str(my_num) + " My favorite number")

# Display nagative to positive
your_num = -10
print(abs(your_num))

# Display 3^2
print(pow(3, 2))

# Display lower number and higher
print(min(5, 2))
print(max(5, 2))

# Display round number
print(round(5.3))
print(round(5.7))

# Import math
from math import *

print(floor(3.7))
print(ceil(3.7))

print(sqrt(36))
print(sqrt(16))

'''
# Display input
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)

# Display input calculate MISTAKE
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2
print(result)

# Display input calculate int
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result_two = int(num1) + int(num2)
print(result_two)

# Display input calcualte float
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result_three = float(num1) + float(num2)
print(result_three)

# Display mad libs game
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print( plural_noun + " are blue")
print("I love " + celebrity)
'''

# Display lists
friends = ["Sok", "Den", "Dang", "Jack\n"]
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])

# Display list two
friends_two = ["Sok", "Den", "Dang", "Jack"]
friends_two[1] = "Coca-cola\n"
print(friends_two[1])

# Display list function
lucky_numbers = [2, 4, 6, 10, 15, 18]
friends_three = ["Sok", "Den", "Dang", "Jack", "WWE"]
"""friends_three.extend(lucky_numbers) # Plust lists and lists"""

"""friends_three.append("Water") # Add name"""

"""friends_three.insert(1, "Mark") # Add name in between"""

"""friends_three.remove("Den") # Remove name"""

"""friends_three.clear() # Remove all name"""

friends_three.pop() # Remove end name

print(friends_three)

# Display count name of lists
friends_four = ["Sok", "Den", "Dang", "Jack", "Jack", "WWE"]
print(friends_four.count("Jack"))

# Display sort a --> z
your_numbers = [12, 32, 12, 3, 5, 34, 20, 18]
your_numbers.sort()
print(your_numbers)

friends_five = ["Sok", "Den", "Dang", "Jack", "Jack", "WWE"]
friends_five.sort()
print(friends_five)

# Copy list
my_list = ["Sok", "Den", "Dang", "Jack", "Jack", "WWE"]
your_list = my_list.copy()
print(your_list)

# Tuples e.g. name_one = (1, 3) NOTE: Tuples use () and Lists use []
coordinates = (4, 5)
print(coordinates[0])
print(coordinates[1])

coordinates = (4, 5)

# Functions
def sayhi():
    print("Hello User")
sayhi()

# Functions two
def say_hi(name):
    print("Hello " + name)

say_hi("Sok")
say_hi("Den")

# Display multiple name and age
def sayhi_two (name, age):
    print("Hello " + name + " you are " + age)

sayhi_two("Sok", "50")
sayhi_two("Den", "20")

# Display multiple name and age
def sayhi_three (name, age):
    print("Hello " + name + " you are " + str(age)) # Convert to str

sayhi_three("Sok", 220)
sayhi_three("Den", 110)

# Return statement
def cube(num):
    return num*num*num
print(cube(3))
print(cube(4))

# Display return two
def cube_two(num_two):
    return num_two*num_two*num_two
result = cube_two(5)
print(result)

# If Statement
is_male = True
if is_male:
    print("You are a male")

# If Statement two
isMale = False
if isMale:
    print("You are a male")
else:
    print("You are not a male")

# Display or 1
isMale_two = True
is_tall = True

if isMale or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male nor tall")

# Display or 2
isMale_three = False
isTall = True

if isMale_three or isTall:
    print("You are a male or tall or both")
else:
    print("You neither male nor tall")

# Display or 3
isMale_four = False
isTall_four = False

if isMale_four or isTall_four:
    print("You are a male or tall or both")
else:
    print("You neither male nor tall")

# Display and 1
isMale_five = True
isTall_five = True

if isMale_five and isTall_five:
    print("You are a tall male\n")
else:
    print("You are either not male or not tall or both\n")

# Display and 2
isMale_six = False
isTall_six = False

if isMale_six and isTall_six:
    print("You are a tall male\n")
elif isMale_six and not(isTall_six):
    print("You are a short male\n")
elif isMale_six and isTall_six:
    print("You are not a male but are tall\n")
else:
    print("You are not a male and not tall\n")

# If Statement & Comparisons (3 parameter)
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))

# 2:00:37