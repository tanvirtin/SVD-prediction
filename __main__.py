from svd import Svd
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

	# Let the movies Matrix, Alien and Serenity be a Sci-fy genre movie and
	# let Casablancas and Amelia be a Romance genre movie

	svd = Svd(dataMatrix)

	svd.svd()

	svd.reduceDimension(2)

	u, d, vTranspose = svd.getSvd()

	# Lets say we have a user Alan who rated these movies 5, 5, 5, 1, and 2.
	# To find what type of movies Alan likes we simply multiply Alan's 1 * n matrix
	# with the matrix v. This will give us a two dimensional matrix telling us
	# what genre of movies Alan prefers. This will transform the user's movies vector
	# into the strength of each movie as v matrix is movies to concepts vector, or
	# in other words n * r matrix

	alanRatings = np.matrix([[5, 5, 5, 1, 2]])

	# Remember the v returned by numpy is already transposed, so we need to 
	# transpose it back to the original v

	alanPreference = np.matmul(alanRatings, np.transpose(vTranspose));

	# printing alanPrefence will show you a 1 * 2 matrix, where each column is the
	# strength of the concept of the database or in other words score of Sci-fi
	# and romance

	print(alanPreference)

	

if __name__ == "__main__":
	main()
