# Create calculator
myNumer1 = int(input("Please enter any number: "))
myOperator = input("Operator: ")
myNumer2 = int(input("Please enter another number: "))

if myOperator == "+":
    print(myNumer1 + myNumer2)
elif myOperator == "-":
    print(myNumer1 - myNumer2)
elif myOperator == "*":
    print(myNumer1 * myNumer2)
elif myOperator == "/":
    print(myNumer1 / myNumer2)
else:
    print("Invalid Operator")