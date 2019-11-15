from GameBoard.connect4 import STANDARD_CONNECT_FOUR_SIZE
from Environment.environment import Env

def test_step():
	player = 1
	action = 0

	total_reward = 0
	env = Env()
	for i in range(3):
		won, reward = env.step(action, player)
		total_reward += reward
		assert(not won and reward == -1)

	won, reward = env.step(action, player)
	assert(won and reward == 100 and env.winner == player)

	env.reset()
	assert(env.winner == 0)


