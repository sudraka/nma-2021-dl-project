import random
import json
import gym
from gym import spaces
import pandas as pd
import numpy as np
from itertools import permutations
from wcst_cards import card_generator


class WCST(gym.Env):
    """WCST Environment that follows gym interface"""

    metadata = {"render.modes": ["human"]}

    def __init__(self):
        """wcst env initiates with observation and action space"""

        super(WCST, self).__init__()

        # define action and observation space
        # must be gym.spaces objects

        # Observations are discrete
        self.observation_space = card_generator()
        # TODO how to incorporate gym.space

        # Actions are discrete:
        N_DISCRETE_ACTIONS = 4  # pick one of the four discrete cards
        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)

    def _rule_env(self):
        """rule of the environment"""
        rule = np.random.choice([0, 1, 2])  # for now
        # TODO more realistic rule, with mean at 3.5
        return rule

    def _next_observation(self):
        """a card is shown with values of (colour, form, num_elements)"""
        wcst_cards = self.observation_space
        card = np.random.choice(wcst_cards)
        return card

    def _take_action(self, obs, policy=None):
        """agent picks one of the four cards based on predefined policy"""

        if policy == None:
            action = self.action_space.sample()  ## random policy, for now
        else:
            action = policy(obs)  ## any other policy based on the observation
        return obs, action

    def _calculalte_reward(self, rule, obs, action):

        right_action = obs[rule]
        reward = +1 if action == right_action else -1

        return reward

    def step(self, obs, policy=None):
        """make one step in the environment"""

        rule = self._rule_env()
        action = self._take_action(obs, policy=None)
        reward = self._calculalte_reward(rule, obs, action)

        self.current_step += 1
        done = self.current_step >= 250  # the game is over after 250 steps

        next_obs = self._next_observation()
        return action, reward, next_obs, done, {}

    def reset(self):
        """reset the state of the environment to the initial state"""
        pass

    def render(self, mode="human", close=False):
        """render the environment to the screen"""
        print(f"Step: {self.current_step}")
        # TODO print more stuff here

    def close(self):
        pass