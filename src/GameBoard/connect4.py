import numpy as np
from typing import Dict, Tuple, Sequence

STANDARD_CONNECT_FOUR_SIZE = (6, 7)
class Board():
    def __init__(self, num_rows: int, num_cols: int):
        assert(num_rows > 4 and num_cols > 4)
        self.board = np.zeros([num_rows, num_cols]).astype(int)
        self.action_space = num_cols


    def shape(self) -> Tuple[int, int]:
        """
        Returns current shape of board

        Returns
        ----------
        (num_rows : int, num_cols : int)
        """
        return self.board.shape


    def apply_action(self, action: int, player: int, train=False):
        """
        Puts player token in a column.

        Parameters
        ----------
        action : int
            action specifying which column to place token in
        player : int
            player id of the token
        train : bool
            bool indicating whether to print boards after each call
        """
        assert(action < self.action_space and self.board[-1][action] == 0 and player != 0)
        for row in range(self.shape()[0]):
            if self.board[row][action] == 0:
                if not train:
                    print("Received player", player)
                self.board[row][action] = player
                if not train:
                    print(self)

                return

    def winner_exists(self) -> Tuple[bool, int]:
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
            print('Found Horizontal Win')
            return won, player

        won, player = self.won_vertical()
        if won:
            print('Found Vertical Win')
            return won, player

        won, player = self.won_diagonal()
        if won:
            print('Found Diagonal Win')
            return won, player

        return False, 0


    def clear(self):
        """
        Removes all tokens frmo the board
        """
        self.board = np.zeros(self.board.shape).astype(int)
        self.action_space = self.board.shape[1]


    def won_horizontal(self) -> Tuple[bool, int]:
        """
        Checks every 4 horizontal consecutive slots to see if someone occupies them. If someone
        does, we will return True and that player.

        Returns
        ----------
        (bool, int)
            returns a tuple where first element is true if someone won and second element
            specifies which player won
        """
        for row in self.board:
            for i in range(len(row)):
                if i+3 > len(row) - 1:
                    continue
                elif row[i] == row[i+1] == row[i+2] == row[i+3] != 0:
                    return True, row[i]
        return False, 0


    def won_vertical(self) -> Tuple[bool, int]:
        """
        Checks every 4 vertical consecutive slots to see if someone occupies them. If someone
        does, we will return True and that player.

        Algorithm
        ----------
        Numpy transposition happens in constant time therefore it is more optimal to simply
        run won_horizontal on the transposed matrix. 

        Returns
        ----------
        (bool, int)
            returns a tuple where first element is true if someone won and second element
            specifies which player won
        """
        try:
            self.board = self.board.T
            return self.won_horizontal()
        finally:
            self.board = self.board.T


    def won_diagonal(self) -> Tuple[bool, int]:
        """
        Checks every 4 diagonal consecutive slots to see if someone occupies them. If someone
        does, we will return True and that player.

        Returns
        ----------
        (bool, int)
            returns a tuple where first element is true if someone won and second element
            specifies which player won
        """
        for x in range(self.shape()[0]):
            for y in range(self.shape()[1]):
            
                if (x+3 < self.shape()[0] and y+3 < self.shape()[1]):
                    if self.board[x][y] == self.board[x+1][y+1] == \
                        self.board[x+2][y+2] == self.board[x+3][y+3] != 0:
                        return True, self.board[x][y]
                if (x+3 < self.shape()[0] and y-3 >= 0):
                    if self.board[x][y] == self.board[x+1][y-1] == \
                        self.board[x+2][y-2] == self.board[x+3][y-3] != 0:
                        return True, self.board[x][y]
        return False, 0


    def is_full(self) -> bool:
        """
        Returns whether connect four board is full

        Returns
        ----------
        bool
        """
        for row in self.board:
            for col in row:
                if col == 0:
                    return False
        return True

    def __str__(self):
        """Returns grid as string form"""
        actions = range(self.action_space)
        s = '-'*(len(self.board[0])*4) + '\n'
        s += '| '
        for row in self.board[::-1]:
            for col in row:
                s += str(col) + ' | '
            s = s[:-3]
            s += '\n'
            s += '-'*len(row)*4 + '\n| '
        s = s[:-2] + '-'*(len(self.board[0])*4) + '\n| '
        for action in actions:
            s += str(action) + ' | '
        return s[:-2] + '\n'
