from GameBoards.connect4 import Board, STANDARD_CONNECT_FOUR_SIZE
def test_board_shape():
	print('Beginning Test for Board Shape')
	# Tests shape of board is true
	b = Board(*STANDARD_CONNECT_FOUR_SIZE)
	# Test board shape
	print('Board Shape Should be {0}, found: {1}'.format(STANDARD_CONNECT_FOUR_SIZE, b.shape()))
	assert(b.shape() == STANDARD_CONNECT_FOUR_SIZE)

	# Test action space
	print('Action Space Should be {0}, found: {1}'.format(STANDARD_CONNECT_FOUR_SIZE[1], b.action_space))
	assert(b.action_space == STANDARD_CONNECT_FOUR_SIZE[1])


def test_board_won_horizontal_or_vertical():
	print('Beginning Test for horizontal and vertical wins')
	b = Board(*STANDARD_CONNECT_FOUR_SIZE)
	# Iterate returns true on every possible win condition
	for i, row in enumerate(b.board):
		for col in range(len(row))[:-4]:

			# Vertical Test
			if i <= len(b.board) - 4:
				b.board[i][col] = b.board[i+1][col] = b.board[i+2][col] = b.board[i+3][col] = 1
				won, player = b.won_vertical()
				print("Expect to find (True, 1), found: {0}".format((won, player)))
				assert(won and player == 1)
				b.clear()

			# Horizontal Test
			b.board[i][col] = b.board[i][col + 1] = b.board[i][col + 2] = b.board[i][col + 3] = 1
			won, player = b.won_horizontal()
			print("Expect to find (True, 1), found: {0}".format((won, player)))
			assert(won and player == 1)
			b.clear()

	won, player = b.won_vertical()
	assert(not won and player == -1)