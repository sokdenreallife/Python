# Exponent Function

def numbers(num1, num2):
    result = 1
    for index in range(num2):
        result = result * num1
    return result
    
print(numbers(2, 3))