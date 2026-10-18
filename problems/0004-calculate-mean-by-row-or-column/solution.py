def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	
	
	total_row = []
	total_col = [] 
	if mode == "row":
		for row in matrix:
			total_row.append(sum(row)/len(row))
		return total_row
	if mode == "column":
		
		for j in range(len(matrix[0])):
			total = 0
			for row in matrix:
				total += row[j]
			total_col.append(total/len(matrix))
		return total_col
				



