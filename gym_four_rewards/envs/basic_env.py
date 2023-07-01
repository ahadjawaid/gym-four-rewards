import gym
from gym import spaces

class FourRewardsEnv(gym.Env):
    def __init__(self):
        self.action_space = spaces.Discrete(5)
        self.observation_space = spaces.Discrete(2)

    def step(self, action):
        state = 1

        reward = 1 if action == 2 else -1
        
        done = True

        info = {}

        return state, reward, done, info

    def reset(self):
        state = 0 
        
        return state