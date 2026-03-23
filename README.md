# Markov Decision Process by gesmorales

## Description
A Markov Decision Process (MDP) is a mathematical framework used to model decision-making in environments where outcomes are partly random and partly under the control of an agent. It is widely applied in reinforcement learning to formalize how an agent interacts with an environment over time (Sutton & Barto, 2020). The defining characteristic of an MDP is the Markov property, which states that the next state depends only on the current state and action, not on prior history (Puterman, 1994).

An MDP is typically represented as a tuple (S, A, P, R, γ). Here, S denotes the set of possible states, A the set of actions available to the agent, P the transition probabilities between states given actions, and R the reward function that provides feedback after each action. The discount factor γ (0 ≤ γ ≤ 1) determines the importance of future rewards relative to immediate ones (Sutton & Barto, 2020). These components collectively define how decisions influence both immediate and future outcomes.

In an MDP, the agent observes a state, selects an action, and transitions to a new state while receiving a reward. This interaction continues sequentially, forming a trajectory of states and actions. The primary objective is to identify an optimal policy, which is a mapping from states to actions that maximizes the expected cumulative reward over time (Puterman, 1994).

## Summary
In simple terms, a Markov Decision Process provides a structured way to model decision-making in uncertain, dynamic environments, enabling systems to learn optimal actions through interaction and feedback.

## Reference
Puterman, M. L. (1994). Markov Decision Processes: Discrete Stochastic Dynamic Programming (1st ed.). Wiley. https://doi.org/10.1002/9780470316887

Sutton, R. S., & Barto, A. (2020). Reinforcement learning: An introduction (Second edition). The MIT Press.

