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


# 00:48:26