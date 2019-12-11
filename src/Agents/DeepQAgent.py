import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch
import heapq
from Agents.Agents import GenericAgent
from GameBoard.connect4 import Board as connect4
import numpy as np
class Model(nn.Module):
    def __init__(self, action_space, observation_space):
        super().__init__()
        feature_space = action_space * observation_space + 1
        self.dense1 = nn.Linear(feature_space, feature_space * 4)
        self.dense2 = nn.Linear(feature_space * 4, feature_space * 4)
        self.output = nn.Linear(feature_space * 4, action_space)

    def forward(self, x):
        h1 = F.relu(self.dense1(x))
        h2 = F.relu(self.dense2(h1))
        return self.output(h2)
    
class DQA(GenericAgent):
    def __init__(self, env, player, alpha=0.01, gamma=0.99, epsilon=0.05):
        super().__init__(env, player)
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.model = Model(self.env.action_space, env.observation_space).to(self.device)
        self.lossfunc = nn.MSELoss()
        self.optimizer = optim.Adam(self.model.parameters(), lr=alpha)

    def policy(self, x, train=True):
        # if len(self.env.valid_actions()) == 0:
        #     print(self.env)
        #     print('Read below debugs')
        #     print('Tie: ', self.env.tie(train=train))
        #     print('Winner? ', self.env.connect4.winner_exists(train=train))
        #     print(self.env)
        #     print(self.env.valid_actions())
        #     print(self.env.connect4.is_full())
        #     print(self.env.winner)
        # assert(len(self.env.valid_actions()) > 0)

        action = None
        xhat = np.concatenate((x, [self.player]))

        xhat = torch.Tensor(xhat).to(self.device)
        bellman_expectations = self.model(xhat)
        reward_expectations = bellman_expectations.tolist()

        
        if train and np.random.uniform() < self.epsilon:
            # epsilon greedy
            action = np.random.choice(self.env.valid_actions())
            expectation = reward_expectations[action]
        else:
            # policy
            heap = reward_expectations.copy()
            heapq.heapify(heap)

            action = float('inf')
            while not self.env.action_is_valid(action):
                expectation = heap.pop()
                action = reward_expectations.index(expectation)
        # bellman_expectations[action].requires_grad = True
        return action, bellman_expectations[action]

    def step(self, state, train=True):
        if type(state) == connect4:
            state = torch.Tensor(state.board.flatten())
        assert(len(state.shape) == 1)
        self.optimizer.zero_grad()

        # Q(s,a) = Q(s,a) + a(r + gamma Q(s+1,a*) - Q(s,a))
        action, expectation = self.policy(state, train=train)
        new_state, reward, done = self.env.step(action, self.player, train=train)
        new_state_modified = torch.Tensor(np.concatenate((new_state.board.flatten(), [self.player]))).to(self.device)
        new_expectation = expectation + self.alpha * (reward + self.gamma * \
            max(self.model(new_state_modified)) - expectation)

        # print('Expectation: {0}, new expectation: {1}, {2}'.format(expectation, new_expectation, type(expectation)))

        loss = self.lossfunc(expectation, new_expectation)
        loss.backward()
        self.optimizer.step()
        return new_state, reward, done

    def save(self):
        torch.save(self.model.state_dict(), './deepq_player{0}'.format(self.player))

    def load(self):
        self.model.load_state_dict(torch.load('./deepq_player{0}'.format(self.player)))

