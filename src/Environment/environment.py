from GameBoard.connect4 import Board, STANDARD_CONNECT_FOUR_SIZE

class Env():
    def __init__(self):
        self.connect4 = Board(*STANDARD_CONNECT_FOUR_SIZE)
        self.winner = 0


    def reset(self):
        """
        Resets the board
        """
        self.connect4.clear()
        self.winner = 0


    def step(self, action: int, player: int):
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
        False, None
            will return this if you gave an invalid action
        False, reward: int
            will return this if episode did not end yet
        True, reward: int
            will return this if episode ended

        """
        if self.winner != 0:
            return True, 100 if player == self.winner else -100

        valid = self.action_is_valid(action)
        if not valid:
            return False, None
        self.connect4.apply_action(action, player)

        won, which_player = self.connect4.winner_exists()
        reward = -1

        if won:
            reward = 100 if player == which_player else -100
            self.winner = which_player
        return won, reward

    def action_is_valid(self, action: int) -> bool:
        """
        Checks to see whether an action can be taken

        Returns
        ----------
        bool
        """
        if action < self.connect4.action_space and self.connect4.board[-1][action] == 0:
            return True
