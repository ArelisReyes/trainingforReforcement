# Import Libraries to Be Used - Do Not Modify This Section
import numpy as np

# -------------------------------------------------------------------------
# List of Mazes

# Basic Example
maze_1 = np.array([[-100., -100., -100., -100., -100., 100., -100., -100., -100., -100., -100.],
                   [-100., -1., -1., -1., -1., -1., -1., -1., -1., -1., -100.],
                   [-100., -1., -100., -100., -100., -100., -100., -1., -100., -1., -100.],
                   [-100., -1., -1., -1., -1., -1., -1., -1., -100., -1., -100.],
                   [-100., -100., -100., -1., -100., -100., -100., -1., -100., -100., -100.],
                   [-1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.],
                   [-100., -100., -100., -100., -100., -1., -100., -100., -100., -100., -100.],
                   [-100., -1., -1., -1., -1., -1., -1., -1., -1., -1., -100.],
                   [-100., -100., -100., -1., -100., -100., -100., -1., -100., -100., -100.],
                   [-1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.],
                   [-100., -100., -100., -100., -100., -100., -100., -100., -100., -100., -100.]])

# Basic Example with Two Goals
maze_2 = np.array([[-100., -100., -100., -100., -100., 100., -100., -100., -100., -100., -100.],
                   [-100., -1., -1., -1., -1., -1., -1., -1., -1., -1., -100.],
                   [-100., -1., -100., -100., -100., -100., -100., -1., -100., -1., -100.],
                   [-100., -1., -1., -1., -1., -1., -1., -1., -100., -1., -100.],
                   [-100., -100., -100., -1., -100., -100., -100., -1., -100., -100., -100.],
                   [100., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.],
                   [-100., -100., -100., -100., -100., -1., -100., -100., -100., -100., -100.],
                   [-100., -1., -1., -1., -1., -1., -1., -1., -1., -1., -100.],
                   [-100., -100., -100., -1., -100., -100., -100., -1., -100., -100., -100.],
                   [-1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.],
                   [-100., -100., -100., -100., -100., -100., -100., -100., -100., -100., -100.]])

# Basic Example with Goal in Another Location
maze_3 = np.array([[-100., -100., -100., -100., -100., -100., -100., -100., -100., -100., -100.],
                   [-100., -1., -1., -1., -1., -1., -1., -1., -1., -1., -100.],
                   [-100., -1., -100., -100., -100., -100., -100., -1., -100., -1., -100.],
                   [-100., -1., -1., -1., -1., -1., -1., -1., -100., -1., -100.],
                   [-100., -100., -100., -1., -100., -100., -100., -1., -100., -100., -100.],
                   [-100., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.],
                   [-100., -100., -100., -100., -100., -1., -100., -100., -100., -100., -100.],
                   [-100., -1., -1., -1., -1., -1., -1., -1., -1., 100., -100.],
                   [-100., -100., -100., -1., -100., -100., -100., -1., -100., -100., -100.],
                   [-1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.],
                   [-100., -100., -100., -100., -100., -100., -100., -100., -100., -100., -100.]])

# Small Example for Observing Q-Value Changes
maze_4 = np.array([[-100, -100, 100],
                   [-1, -1, -1],
                   [1, -1, -1]])

# Zigzag Example
maze_5 = np.array([[-100., -100., -100., -100., -100., -100., -100., -100., -100., -100.],
                   [100., -1., -1., -1., -1., -1., -1., -1., -1., -100.],
                   [-100., -100., -100., -100., -100., -100., -100., -100., -1., -100.],
                   [-100., -1., -1., -1., -1., -1., -1., -1., -1., -100.],
                   [-100., -1., -100., -100., -100., -100., -100., -100., -100., -100.],
                   [-100., -1., -1., -1., -1., -1., -1., -1., -1., -100.],
                   [-100., -100., -100., -100., -100., -100., -100., -100., -1., -100.],
                   [-100., -1., -1., -1., -1., -1., -1., -1., -1., -100.],
