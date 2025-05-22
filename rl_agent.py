# Re-running the RL agent setup code after state reset

import numpy as np
import random

class QLearningAgent:
    def __init__(self, maze, start, goal, alpha=0.1, gamma=0.9, epsilon=0.2, episodes=1000):
        self.maze = maze
        self.start = start
        self.goal = goal
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.episodes = episodes
        self.rows, self.cols = len(maze), len(maze[0])
        self.actions = ['up', 'down', 'left', 'right']
        self.q_table = {}
        self._init_q_table()

    def _init_q_table(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.maze[i][j] == 0:
                    self.q_table[(i, j)] = {a: 0.0 for a in self.actions}

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        else:
            return max(self.q_table[state], key=self.q_table[state].get)

    def get_next_state(self, state, action):
        x, y = state
        if action == 'up': x -= 1
        elif action == 'down': x += 1
        elif action == 'left': y -= 1
        elif action == 'right': y += 1

        if 0 <= x < self.rows and 0 <= y < self.cols and self.maze[x][y] == 0:
            return (x, y)
        return state

    def train(self):
        for _ in range(self.episodes):
            state = self.start
            while state != self.goal:
                action = self.choose_action(state)
                next_state = self.get_next_state(state, action)
                reward = 10 if next_state == self.goal else -0.1
                best_next_action = max(self.q_table[next_state], key=self.q_table[next_state].get)
                td_target = reward + self.gamma * self.q_table[next_state][best_next_action]
                td_delta = td_target - self.q_table[state][action]
                self.q_table[state][action] += self.alpha * td_delta
                state = next_state

    def extract_path(self):
        path = []
        state = self.start
        visited = set()
        while state != self.goal:
            path.append(state)
            visited.add(state)
            action = max(self.q_table[state], key=self.q_table[state].get)
            next_state = self.get_next_state(state, action)
            if next_state in visited:
                break
            state = next_state
        path.append(self.goal)
        return path

# Exportable interface
def train_q_agent(maze, start, goal, episodes=1000):
    agent = QLearningAgent(maze, start, goal, episodes=episodes)
    agent.train()
    return agent.extract_path()
