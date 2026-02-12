import random
from collections import defaultdict


class QLAgent:
    def __init__(self, actions, alpha, gamma, epsilon):
        self.Q = defaultdict(float)
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    #
    def get_q(self, state, action):
        return self.Q[(state,action)]

    # function to choose an action
    # we can either explore by chosing a random action
    # or exploit by chosing the best action based on the Q value
    def choose_action(self, state, valid_actions):
        if random.random() < self.epsilon:
            return random.choice(valid_actions)
        qs = {}
        for a in valid_actions:
            qs[a] = self.get_q(state, a)

        if max(qs.values()) == 0:
            return random.choice(valid_actions)

        return max(qs, key=qs.get)

    #
    def learn(self, s, a, r, s_next, next_actions):
        best_future_q = 0
        if next_actions:
            best_future_q = max(self.get_q(s_next, a2) for a2 in next_actions)

        old_q = self.get_q(s, a)

        self.Q[(s,a)] = old_q + self.alpha * (r + self.gamma * (best_future_q-old_q))

    