from Agents.Agents import GenericAgent
class HA(GenericAgent):
    def step(self, state, train=True):
        print(self.env)
        action = int(input('Choose a possible action: {0}'.format(self.env.valid_actions())))
        return self.env.step(action, self.player, train=train)
