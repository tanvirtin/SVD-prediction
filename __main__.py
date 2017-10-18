from SVD import SVD
import numpy as np

def main():
	# In this m * n matrix, m is the user and, n is the movies
	# The movies are Matrix, Alien, Serenity, Casablancas and Amelia
	dataMatrix = np.matrix([
		[1, 1, 1, 0, 0], 
		[3, 3, 3, 0, 0], 
		[4, 4, 4, 0, 0], 
		[5, 5, 5, 0, 0], 
		[0, 2, 0, 4, 4],
		[0, 0, 0, 5, 5],
		[0, 1, 0, 2, 2]
		])

	svd = SVD(dataMatrix)

	svd.svd()

	svd.reduceDimension(2)

	u, d, v = svd.getSvd()

	print(d)

if __name__ == "__main__":
	main()