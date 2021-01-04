# Variables
character_name = "Den"
character_age = str(21)

print("There once was a man named " + character_name + ".")
print("He was " + character_age + " years old.")
print("He really liked the name " + character_name + ".")
print("But didn't like being " + character_age +".\n")

# I can also using variables with "," symbol
characterName = "Sok"
characterAge = "21"

print("You are so smart", characterName,".")
print("In this year you have age", characterAge ,"-year-old.\n")

# How I display text lowercase and uppercase
phrase = "Hello how are you?"

print(phrase.lower()) # It's display lowercase
print(phrase.upper()) # It's display uppercase

# Strings (display indexs)
greeting = "Hello"

print(greeting[0]) # Read from left to right start with 0
print(greeting[-1]) # Read from right to left start with -1

print(len(greeting)) # Count letters

print(greeting.find("llo")) # Find similar letters
print(greeting.find("b")) # I don't know this problem that is show nagative -1

print(greeting[1:]) # Colon ":" meaning count start from 1 to end of letters
print(greeting[2:5]) # Colon ":" meaning count start from 2 to 4 of letters

print("Enter line\n")

# Math (Integers & Float)
print( 5 * 5) # Meaning 5 * 5 = 25
print( 5 ** 5) # Meaning 5^5 = 3125
print( 2 + 3 * 5) # Apply multiplication first: order of operations
print( 25 % 2) # Take remains: returns remainder of 25/2
print(10 / 3.0)      # int's and doubles

num = 10
num += 100 # +=, -=, /=, *=
print(num)

"""
num_one = 20
++num_one # Python can not perform, but not show error when RUN program
print(num_one)
"""

# Math module has useful math methods
import math
print( pow(2, 3) )
print( math.sqrt(144) )
print( round(2.7) )