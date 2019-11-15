from GameBoard.connect4 import Board, STANDARD_CONNECT_FOUR_SIZE
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
                won, player = b.winner_exists()
                assert(won and player == 1)
                b.clear()

            # Horizontal Test
            b.board[i][col] = b.board[i][col + 1] = b.board[i][col + 2] = b.board[i][col + 3] = 1
            won, player = b.winner_exists()
            assert(won and player == 1)
            b.clear()

    won, player = b.winner_exists()
    assert(not won and player == 0)


def test_board_diagonal_wins():
    print('Beginning Test for diagonal wins')
    b = Board(*STANDARD_CONNECT_FOUR_SIZE)
    for x in range(b.shape()[0]):
        for y in range(b.shape()[1]):
        
            if (x+3 < b.shape()[0] and y+3 < b.shape()[1]):
                b.board[x][y] = b.board[x+1][y+1] = b.board[x+2][y+2] = b.board[x+3][y+3] = 1
                won, player = b.winner_exists()
                assert(won and player == 1)
                b.clear()

            if (x+3 < b.shape()[0] and y-3 >= 0):
                b.board[x][y] = b.board[x+1][y-1] = b.board[x+2][y-2] = b.board[x+3][y-3] = 1
                won, player = b.winner_exists()
                assert(won and player == 1)
                b.clear()
    won, player = b.winner_exists()
    assert(not won and player == 0)


def test_is_full():
    print('Testing whether the board is full works')
    b = Board(*STANDARD_CONNECT_FOUR_SIZE)
    for x in range(b.shape()[0]):
        for y in range(b.shape()[1]):
            b.apply_action(y, 1)
    assert(b.is_full())
