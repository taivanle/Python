#2D lists and nested loops

matrix_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in matrix_grid:
    for col in row:
        print(col)
#the code above is a nested for loop where we have used a for loop within a for loop

#print(matrix_grid[0][3]) # the first [] shows in the index which is the row, the second[] shows the collumn
#here we have made a list using the [] BUT we have created further lists inside of them which are shown through []