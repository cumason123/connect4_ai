from GameBoard.connect4 import STANDARD_CONNECT_FOUR_SIZE
from Environment.environment import Env

def test_simple_win():
	player = 1
	action = 0

	total_reward = 0
	env = Env()
	for i in range(3):
		state, reward, won = env.step(action, player)
		total_reward += reward
		assert(not won and reward == -1)

	state, reward, won = env.step(action, player)
	assert(won and reward == 100 and env.winner == player and \
		state.shape() == (env.observation_space,env.action_space))

	env.reset()
	assert(env.winner == 0)


def test_diagonal_step_win():
	player = 1
	action = 0
	env = Env()

	env.step(0, player)
	env.step(0, player)
	env.step(0, 2)
	state, reward, won = env.step(0, player)
	print(won, reward, env.winner)
	assert(not won and reward == -1)

	env.step(1, 2)
	env.step(1, 2)
	env.step(1, player)	

	env.step(2, player)
	state, reward, won = env.step(2, player)
	assert(not won and env.winner == 0 and reward == -1)

	state, reward, won = env.step(3, player)
	assert(won and env.winner == player and reward == 100)


def test_valid_actions():
	player = 1
	action = 0
	env = Env()
	for i in range(6):
		state, reward, won = env.step(0, player)
		player = 2 if player == 1 else 1
		assert(not won and reward == -1)
	assert(not env.action_is_valid(0))
