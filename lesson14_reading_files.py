# # Reading Files
# # របៀបមើលអែកសារ (.text) អានបាន ឬមិនបាន (True or False)
# employee_file = open("employees.txt", "r") # ("r": meant read) ("w": meant write និងលុបអក្សរនៅក្នុងអែកសារ (.text))

# print(employee_file.read()) # .read(), .readline(), .readlines(), .readable()

# # Read and the stop (ប្រសិនបើយើងមិនដាក់វាទេ នោះវានឹងដំណើរការរហូត)
# employee_file.close()

"""========================================"""

employee_file = open("employees.txt", "r")

for employee in employee_file.readlines():
    print(employee)

employee_file.close()