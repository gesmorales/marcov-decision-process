# Markov Decision Process by gesmorales

## Description
A Markov Decision Process (MDP) is a mathematical framework used to model decision-making in environments where outcomes are partly random and partly under the control of an agent. It is widely applied in reinforcement learning to formalize how an agent interacts with an environment over time (Sutton & Barto, 2020). The defining characteristic of an MDP is the Markov property, which states that the next state depends only on the current state and action, not on prior history (Puterman, 1994).

An MDP is typically represented as a tuple (S, A, P, R, γ). Here, S denotes the set of possible states, A the set of actions available to the agent, P the transition probabilities between states given actions, and R the reward function that provides feedback after each action. The discount factor γ (0 ≤ γ ≤ 1) determines the importance of future rewards relative to immediate ones (Sutton & Barto, 2020). These components collectively define how decisions influence both immediate and future outcomes.

In an MDP, the agent observes a state, selects an action, and transitions to a new state while receiving a reward. This interaction continues sequentially, forming a trajectory of states and actions. The primary objective is to identify an optimal policy, which is a mapping from states to actions that maximizes the expected cumulative reward over time (Puterman, 1994).

## Frozen Lake (Slippery Grid) (Markov Decision Process Example 1)

### Overview
frozenlake.py - this project demonstrates a Markov Decision Process (MDP) using the Frozen Lake environment. The agent learns how to navigate a grid world with uncertain (stochastic) transitions, where movements may not always go as intended due to a slippery surface.

The objective is to reach the goal while avoiding holes by learning an optimal policy through reinforcement learning.

### MDP Components
- States (S): Grid positions on the lake
- Actions (A): Left, Right, Up, Down
- Transition Probability (P): Stochastic (slippery movement)
- Reward Function (R):
    - Goal = +1
    - Hole = 0
- Other states = 0
- Discount Factor (γ): Controls importance of future rewards

### Algorithm Used
Q-Learning
- Model-free reinforcement learning algorithm
- Learns optimal action-value function (Q-table)
- Balances exploration vs exploitation

### Expected Output
- The agent trains over multiple episodes
- Q-table is updated based on rewards
- Final run shows the learned path to the goal
- Output includes:
    - Grid rendering
    - Final reward (1 if successful, 0 otherwise)

## Traffic Light Control (Markov Decision Process Example 2)

### Overview
trafficlight.py - this project simulates a traffic light control system using a Markov Decision Process (MDP). The goal is to reduce traffic congestion by allowing an agent to decide whether to keep or switch traffic lights based on current traffic conditions.

### MDP Components
- States (S):
    - 0 = Low traffic
    - 1 = Medium traffic
    - 2 = High traffic
- Actions (A):
    - 0 = Keep current light
    - 1 = Switch light
- Transition (P):
    - Traffic changes dynamically and may improve or worsen
- Reward (R):
    - Low traffic = +2
    - Medium traffic = -1
    - High traffic = -5

### Algorithm Used
Q-Learning
    - Learns optimal actions without needing a model of the environment
    - Uses a Q-table to estimate action values

### Expected Output
- Displays the learned Q-table
- Shows optimal action for each traffic state

## Summary
In simple terms, a Markov Decision Process provides a structured way to model decision-making in uncertain, dynamic environments, enabling systems to learn optimal actions through interaction and feedback.

## Reference
Puterman, M. L. (1994). Markov Decision Processes: Discrete Stochastic Dynamic Programming (1st ed.). Wiley. https://doi.org/10.1002/9780470316887

Sutton, R. S., & Barto, A. (2020). Reinforcement learning: An introduction (Second edition). The MIT Press.

