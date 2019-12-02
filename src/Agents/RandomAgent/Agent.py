import sys
sys.path.append('..')
from Environment.environment import Env
import numpy as np
class RA():
	def __init__(self, player, env):
		self.env = env
		self.player = player

	def step(self):
		valid_actions = self.env.valid_actions()
		taken_action = np.random.choice(valid_actions)
		return self.env.step(taken_action, self.player)