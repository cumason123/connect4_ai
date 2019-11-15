from GameBoards.connect4 import Board
def test_board():
	b = Board(5,5)
	assert(b.board.shape == (5,5))