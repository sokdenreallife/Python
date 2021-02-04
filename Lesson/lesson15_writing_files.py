# Writing Files
# របៀបបន្ថែមពាក្យចូលទៅក្នុងហ្វាល់ (.text)
# also try "a" for append
employee_file = open("employee_file", "a") # បើប្រើពាក្យ "w" នោះនឹងលុបហ្វាល់ចាស់ចោល ឬ Overrite existing file

employee_file.write("\nHello Den Sok")

employee_file.close()