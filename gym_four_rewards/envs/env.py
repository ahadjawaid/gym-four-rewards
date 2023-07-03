import gym
from gym import spaces

class FourRewardsEnv(gym.Env):
    def __init__(self, n_steps: int) -> None:
        self.N_ACTIONS = 2
        self.N_STATES = 9
        self.START_STATE = 4
        self.STEP_LIMIT = n_steps

        self.states_with_rewards = {0: 3, 2: 2, 5: 1, 8: 4}
        self.current_time_step = 0

        self.action_space = spaces.Discrete(self.N_ACTIONS, start=self.START_STATE)
        self.observation_space = spaces.Discrete(self.N_STATES)

        self.state = self.START_STATE

    def _transition(self, action: int) -> int:
        new_state = self.state - (action if action == 1 else -1)

        if new_state >= self.N_STATES or new_state < 0:
            return self.state
        
        return new_state

    def _reward(self, state: int) -> int:
        return self.states_with_rewards.get(state, 0)

    def step(self, action):
        new_state = self._transition(action)
        self.state = new_state

        reward = self._reward(new_state)

        self.current_time_step += 1
        done = self.STEP_LIMIT >= self.current_time_step

        info = {}

        return new_state, reward, done, info

    def reset(self):
        self.state = self.START_STATE
        
        return self.state