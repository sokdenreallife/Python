# Classes & Objects

# This is the class
class Book:
  def __init__(self, title, author, numPages):
      self.title = title
      self.author = author
      self.numPages = numPages


# This is the Objects
book1 = Book("Harry Potter", "JK Rowling", 500)
book2 = Book("Sok", "Den", 21)
book1.title = "Half-Blood Prince"

print(book1.title)
print(book2.numPages)

# ចាំណាំ៖ យើងអាចបង្កើតខ្លាស់នៅហ្វាល់ទី១ ហើយយកអប់ជេកបង្កើតក្នុងហ្វាល់ទី២ ដើម្បីបង្ហាញទិន្នន័យ (from ឈ្មោះហ្វាល់ទី២ import ឈ្មោះខ្លាស់)