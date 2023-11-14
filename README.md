# Maze Solver with Q-Learning

This Python project demonstrates a maze-solving AI using Q-learning. The AI learns to navigate through a maze by assigning quality values (Q-values) to different actions in each square of the maze. The Q-learning algorithm is then used to update these values based on the rewards obtained during the exploration of the maze.

## Project Overview

- **Maze Representation:** The maze is represented as a grid, where each cell can be either a wall, an empty space, or the goal.

- **Q-Learning:** The Q-learning algorithm is employed to train the AI. The AI explores the maze, and at each step, it updates the Q-values based on the rewards obtained and the best possible actions.

- **Training:** The AI is trained by having it solve the maze multiple times. The training loop allows the AI to learn the optimal path to reach the goal.

- **Visualization:** The pygame library is used for visualization. The maze, player, and goal are displayed graphically, allowing for interactive observation of the AI's navigation.

- **Shortest Path:** After training, the AI can find and visualize the shortest path from a given starting position to the goal.

## Instructions

1. **Dependencies:** Make sure to install the required dependencies using `pip install pygame`, `pip install numpy`.

2. **Run the Code:** Execute the Python script to train the AI and observe its performance in solving the maze.

3. **Visualization:** After training, the AI will demonstrate the shortest path from various starting positions to the goal.

4. **Close the Game:** The pygame window can be closed after observing the results.

Feel free to experiment with different mazes and parameters to observe how the AI adapts to various scenarios.

This project serves as a practical implementation of Q-learning in a maze-solving context and provides a hands-on experience with reinforcement learning concepts.
