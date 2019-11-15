import numpy as np
class Board():
	def __init__(self, num_rows, num_cols):
		self.board = np.zeros([num_rows, num_cols])

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

	def won_horizontal(self):
		return False, -1

	def won_vertical(self):
		return False, -1