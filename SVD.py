import numpy as np

class SVD:
	def __init__(self, dataMatrix):
		self.dataMatrix = dataMatrix
		self.u = None
		self.d = None
		self.v = None

	def svd(self):
		self.u, self.d, self.v = np.linalg.svd(self.dataMatrix)

		# the d that we get is undiagonalized meaning only the columns containing
		# non zeroes are represented in a 1 * r matrix where r is the number of non
		# zero values
		self.d = np.diag(self.d)

		# after doing the svd, we obtain 3 matrices u, d and v, the matrix u is 
		# m * r, meaning users to concepts matrix, where concept is the strength of the
		# dataset, or the measurement of the strength of the genre that this dataset
		# is broken down into. The matrix d is a r * r matrix and the d matrix is the
		# movies to concept matrix or n * r matrix.

		# The u, d, v will generally have some noise associated with it, to remove the
		# noise we need to reduce the dimension of the matrix. From our dataset we can
		# notice that our dataset is broken down into two concepts or r. The two concepts
		# are the genre Romance and the genre Sci-fi. The columns of u, d and v are 
		# represening the genre of the movies, so we can reduce the dimension by reducing
		# the number of columns


	def reduceDimension(self, amount):
		self.u = self.u[:, 0:amount]

		# Since it is a r * r matrix we not only have to remove one of the columns,
		# but also the row of the matrix
		self.d = self.d[0:amount, 0:amount]

		# the v that we get is already transpose, so we simply transpose it back
		# reduce the dimension and tranpose it again
		self.v = np.transpose(self.v)

		self.v = self.v[:, 0:amount]

		self.v = np.transpose(self.v)


	def getSvd(self):
		return (self.u, self.d, self.v)