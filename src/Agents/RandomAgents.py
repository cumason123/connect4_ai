import sys
sys.path.append('..')
from Environment.environment import Env
from Agents.Agents import GenericAgent
import numpy as np
class RA(GenericAgent):
	def step(self, state, train=False):
		valid_actions = self.env.valid_actions()
		taken_action = np.random.choice(valid_actions)
		return self.env.step(taken_action, self.player)