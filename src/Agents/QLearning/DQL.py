import torch
import torchvision

class deepq():
	def __init__(self, env)
		feature_space = env.action_space * env.observation_space

		self.network = torch.nn.Sequential(
			torch.nn.Linear(feature_space, feature_space*2),
			torch.nn.Relu(),
			torch.nn.Linear(feature_space*2, feature_space*2),
			torch.nn.Relu(),
			torch.nn.Linear(feature_space*2, env.action_space)
		)
	def policy(self, x):
		action = self.network(x)