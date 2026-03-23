import numpy as np
import random

# States: 0 = low traffic, 1 = medium, 2 = high
states = [0, 1, 2]
actions = [0, 1]  # 0 = keep, 1 = switch

q_table = np.zeros((len(states), len(actions)))

# Hyperparameters
alpha = 0.1
gamma = 0.9
epsilon = 1.0
epsilon_decay = 0.995
min_epsilon = 0.01
episodes = 1000

def get_reward(state):
    if state == 0:
        return 2   # low traffic = good
    elif state == 1:
        return -1
    else:
        return -5  # high traffic = bad

def next_state(state, action):
    # Simulate random traffic change
    if action == 1:  # switching improves traffic
        return max(0, state - 1)
    else:
        return min(2, state + random.choice([-1, 0, 1]))

# Training loop
for episode in range(episodes):
    state = random.choice(states)
    done = False

    for _ in range(20):  # steps per episode
        if random.uniform(0, 1) < epsilon:
            action = random.choice(actions)
        else:
            action = np.argmax(q_table[state])

        new_state = next_state(state, action)
        reward = get_reward(new_state)

        # Q-learning update
        q_table[state, action] += alpha * (
            reward + gamma * np.max(q_table[new_state]) - q_table[state, action]
        )

        state = new_state

    epsilon = max(min_epsilon, epsilon * epsilon_decay)

print("Training complete!\n")
print("Q-table:\n", q_table)

# Test policy
print("\nTesting learned policy:")
for state in states:
    action = np.argmax(q_table[state])
    print(f"State {state} -> Action {action}")
