def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	n_features = len(vectors)
	n_obs = len(vectors[0])

	mean = []
	for features in vectors:
		mean.append(sum(features)/n_obs)
	
	cov = []
	for i in range(n_features):
		row = []
		for j in range(n_features):
			total = 0
			for k in range(n_obs):
				total += (vectors[i][k] - mean[i])*(vectors[j][k] - mean[j])
			row.append(total/(n_obs-1))
		cov.append(row)

	return cov