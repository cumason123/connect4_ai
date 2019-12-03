class GenericAgent():
	def __init__(self, env, player):
		self.env = env
		self.player = player
		
	def __str__(self):
		return '{0} player {1}'.format(type(self).__name__, self.player)
