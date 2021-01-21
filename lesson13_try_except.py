# # Find error in code

# try:
#     input_integerOnly = int(input("Enter number: "))
#     print(input_integerOnly)
# except:
#     print("Invalid Number is String")

###############################################

# code asks user for number and divides 10 by it
# enter '0' to trigger exception
try:
    answer = 10 / int(input("Enter Number: "))
except ZeroDivisionError as e:
    print(e)
except:
    print("Caught any exception")
