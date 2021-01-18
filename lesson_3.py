# # Create a calculation
# calNumber1 = int(input("Enter number: "))
# calNumber2 = int(input("Enter another number: "))

# plusA = int(calNumber1 + calNumber2)
# plusB = calNumber1 - calNumber2
# plusC = calNumber1 * calNumber2
# plusD = calNumber1 / calNumber2
# plusD = calNumber1 % calNumber2

# print("Your plus =", plusA)
# print("Your minus = ", plusB)
# print("Your multiple=", plusC)
# print("Your divide =", plusD)
# print("Your % =", plusD)

# friends = []
# friends.append("Oscar")
# friends.append("Angela")
# friends.insert(2, "Kevin")

# # friends.remove("Kevin")
# print( friends )
# print( friends.index("Oscar") )
# print( friends.count("Angela") )
# friends.sort()
# print( friends )
# friends.clear()
# print( friends )

# # Lists
# lucky_numbers = [4, 8, "fifteen", 16, 23, 42.0, 16, 43.0]

# print(lucky_numbers[2])
# print(len(lucky_numbers))

# # Turples
# myNumber = (2, 3, "Sok", 23, 43, "Den")
# # indexs    0   1   2     3   4    5

# print(myNumber[0])
# print(myNumber[2])
# print(myNumber[3])
# print(myNumber[4])

# # Function
# def main(name, age):
#     print("Hello Sok " + name + " Your age is " + str(age) + " Year old.")

# main("Den", 21)

# # Return Statements
# def add_numbers(num1, num2, num3):
#     return num1 + (num2 * num3)

# calculate = add_numbers(3, 2, 5)
# print(calculate)

# Calcualte using IF, Elif and Else
enterNumber1 = int(input("Enter any number: "))
operation = input("Operator: ")
enterNumber2 = int(input("Enter another number: "))

if operation == "+":
    print(enterNumber1 + enterNumber2)
elif operation == "-":
    print(enterNumber1 - enterNumber2)
elif operation == "*":
    print(enterNumber1 * enterNumber2)
elif operation == "/":
    print(enterNumber1 / enterNumber2)
elif operation == "%":
    print(enterNumber1 % enterNumber2)