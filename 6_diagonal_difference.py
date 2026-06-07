def diagonal_difference(matrix):
	n = len(matrix)
	primary = 0
	secondary = 0
	for i in range(n):
		primary += matrix[i][i]
		secondary += matrix[i][n - 1 - i]
	return abs(primary - secondary)

matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonal_difference(matrix))

