import numpy as np
STANDARD_CONNECT_FOUR_SIZE = (6, 7)
class Board():
	def __init__(self, num_rows, num_cols):
		self.board = np.zeros([num_rows, num_cols])
		self.action_space = num_cols

	def shape(self):
		# Returns shape of board
		return self.board.shape

	def winner_exists(self):
		"""
		Checks to see if a player has won. If no players have won, return false and -1

		Returns
		----------
		(bool, int)
			returns a tuple where first element is true if someone won and second element
			specifies which player won
		"""
		won, player = self.won_horizontal()
		if won:
			return won, player

		won, player = self.won_vertical()
		if won:
			return won, player

		won, player = self.won_diagonal()
		if won:
			return won, player

		return False, -1

	def clear(self):
		"""
		Removes all tokens frmo the board
		"""
		self.board = np.zeros(self.board.shape)
		self.action_space = self.board.shape[1]

	def won_horizontal(self):
		for row in self.board:
			for i in range(len(row)):
				if i+3 > len(row) - 1:
					continue
				elif row[i] == row[i+1] == row[i+2] == row[i+3] != 0:
					return True, row[i]
		return False, -1

	def won_vertical(self):
		try:
			self.board = self.board.T
			return self.won_horizontal()
		finally:
			self.board = self.board.T

