import gym
import numpy as np

# Create Frozen Lake environment
env = gym.make("FrozenLake-v1", is_slippery=True)

# Initialize Q-table
state_size = env.observation_space.n
action_size = env.action_space.n
q_table = np.zeros((state_size, action_size))

# Hyperparameters
alpha = 0.8        # learning rate
gamma = 0.95       # discount factor
epsilon = 1.0      # exploration rate
epsilon_decay = 0.995
min_epsilon = 0.01
episodes = 2000

# Training using Q-learning
for episode in range(episodes):
    state = env.reset()[0]
    done = False

    while not done:
        if np.random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state, :])

        new_state, reward, done, _, _ = env.step(action)

        # Q-learning update
        q_table[state, action] = q_table[state, action] + alpha * (
            reward + gamma * np.max(q_table[new_state, :]) - q_table[state, action]
        )

        state = new_state

    epsilon = max(min_epsilon, epsilon * epsilon_decay)

print("Training finished!\n")

# Test the trained agent
state = env.reset()[0]
done = False

env.render()

while not done:
    action = np.argmax(q_table[state, :])
    state, reward, done, _, _ = env.step(action)
    env.render()

print("Final Reward:", reward)
