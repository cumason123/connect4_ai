from GameBoard.connect4 import Board, STANDARD_CONNECT_FOUR_SIZE

class Env():
    def __init__(self):
        self.connect4 = Board(*STANDARD_CONNECT_FOUR_SIZE)
        self.winner = 0
        self.observation_space = self.connect4.board.shape[0]
        self.action_space = self.connect4.board.shape[1]
        self.actions = []


    def reset(self):
        """
        Resets the board
        """
        self.connect4.clear()
        self.winner = 0


    def undo(self):
        if self.actions == []:
            return False
        elif self.winner != 0:
            self.winner = 0
        row, col = self.actions.pop()
        self.connect4[row][col] = 0
        return True

    def valid_actions(self):
        return [action for action in range(self.action_space) if self.action_is_valid(action)]

    def step(self, action: int, player: int, train=False):
        """
        Agent takes action in environment only if action is takeable.

        Parameters
        ----------
        action : int
            action to take
        player : int
            player id

        Returns
        ----------
        state, reward, done

        """
        if self.winner != 0:
            return self.connect4, 100 if player == self.winner else -100, True
        if self.tie(train=train):
            return self.connect4, 0, True

        assert(self.action_is_valid(action))
        self.connect4.apply_action(action, player, train=train)

        finished, which_player = self.connect4.winner_exists(train=train)

        if finished:
            self.winner = which_player
            return self.connect4, 100 if player == self.winner else -100, finished

        return self.connect4, -1, finished

    def action_is_valid(self, action: int) -> bool:
        """
        Checks to see whether an action can be taken

        Returns
        ----------
        bool
        """
        if action < self.connect4.action_space and self.connect4.board[-1][action] == 0:
            return True
        return False

    def tie(self, train=False) -> bool:
        return not self.connect4.winner_exists(train=train) and self.connect4.is_full()

    def __str__(self):
        return str(self.connect4)
