# 1. 2d Arrays & Nested Loops
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# Display all element
for row in number_grid:
    for col in row:
        print(col)





# 2. Copy from Mike Dance
number_grid = [ [1, 2], [3, 4] ]

number_grid[0][1] = 99
print(number_grid[0][0])
print(number_grid[0][1])

for rows in number_grid:
     for cols in rows:
          print(cols)