import random
import numpy as np
class QLearningAgent:
    def __init__(self,player,alpha = 0.1 ,gamma= 0.9,epsilon = 0.2):
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon  = epsilon
        self.player = player

    def get_q_value(self,state,action):
        return self.q_table.get((state,action),0.0)

    def choose_action(self,state,available_actions):
        if random.random() < self.epsilon:
            return random.choice(available_actions)
        else:
            q_values = [self.get_q_value(state,a) for a in available_actions]
            max_q = max(q_values)
            max_actions = [a for a ,q in zip(available_actions,q_values) if q == max_q]
            return random.choice(max_actions)

    def update(self,state,action,reward,next_state,next_action):
        old_q = self.get_q_value(state, action)
        if next_action:
            future_q = max([self.get_q_value(next_state,a) for a in next_action])
        else:
            future_q = 0.0

        new_q = old_q + self.alpha*(reward+ self.gamma*future_q-old_q)

        self.q_table[(state,action)] = new_q
