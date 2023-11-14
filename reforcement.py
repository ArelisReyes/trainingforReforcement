# Import libraries to be used - do not modify this section
import pygame
from pygame.locals import *
import numpy as np
from time import sleep
import lab

# -------------------------------------------------------------------------

# Rewards - Choose a maze to use
rewards = mazes.maze_1

# Maze size (rewards)
rows = rewards.shape[0]
columns = rewards.shape[1]

# Image and window sizes
size = 32  # Size of images (player.jpg, goal.jpg, wall.jpg)
window_height = columns * size
window_width = rows * size

# Initialize pygame and create window
pygame.init()
window = pygame.display.set_mode((window_height, window_width), pygame.HWSURFACE)

# Load images of the wall, player, and goal
img_wall = pygame.image.load("Images/Wall.jpg").convert()
img_player = pygame.image.load("Images/Player.jpg").convert()
img_goal = pygame.image.load("Images/Goal.jpg").convert()

# Function to draw the current state of the maze and the player's position
def draw_maze(player_x, player_y):
    for i in range(0, rewards.shape[0]):
        for j in range(0, rewards.shape[1]):
            if rewards[i, j] == -100:
                window.blit(img_wall, (j * size, i * size))
            if rewards[i, j] == 100:
                window.blit(img_goal, (j * size, i * size))
    window.blit(img_player, (player_y * size, player_x * size))

# -------------------------------------------------------------------------

# Define the end condition
# If the reward is -1 (an empty square), the game continues
# If it hits a wall (loses) or reaches the goal (wins), the game ends
def end_game_condition(current_row, current_column):
    if rewards[current_row, current_column] == -1.:
        return False
    else:
        return True

# Start the game from a random position
def initial_point():
    while True:
        # Find a row and column value to start the game
        current_row = np.random.randint(rows)
        current_column = np.random.randint(columns)

        # If the chosen position is not a wall or the goal, stop the search and use that value
        if not end_game_condition(current_row, current_column):
            break

    # Return the found result
    return current_row, current_column

# This function helps us choose an action easily and calculate the new position using only one number
def next_point(current_row, current_column, action_index):
    # Save the current values
    new_row = current_row
    new_column = current_column

    # Actions: 0 = up, 1 = right, 2 = down, 3 = left
    actions = ['up', 'right', 'down', 'left']

    # Then modify the row or column corresponding to the action
    if actions[action_index] == 'up' and current_row > 0:
        new_row -= 1
    elif actions[action_index] == 'right' and current_column < columns - 1:
        new_column += 1
    elif actions[action_index] == 'down' and current_row < rows - 1:
        new_row += 1
    elif actions[action_index] == 'left' and current_column > 0:
        new_column -= 1

    # Finally, return the new position
    return new_row, new_column

# -------------------------------------------------------------------------

# Create a table with the Q values (Q, quality in English) that will help us decide the best action in each square.
# So we will have 4 values for each row and column of the maze (one for each action).
q_values = np.zeros((rows, columns, 4))

# Training parameters
exploration = 0.1   # Percentage of times we will try something new (keep it below 0.2 - 20%)
discount = 0.9  # Percentage with which we will discount future rewards
learning = 0.9  # Learning rate, i.e., how much

# It is a function that helps us explore new possibilities or use the knowledge we already have
# for this, it uses the explore parameter, which is a percentage that helps us decide how many times we are going
# to use random values and how many times we are going to use the best answers we have
def next_action(current_row, current_column, explore):
    # if a randomly chosen value between 0 and 1 is less than epsilon,
    # then choose the most promising value from the Q-table for this state.
    if np.random.random() > explore:
        # Use the argmax function to find the best action (the highest number)
        return np.argmax(q_values[current_row, current_column])
    else:
        # Use the random function to choose a random number
        return np.random.randint(4)

# -------------------------------------------------------------------------
# GAME - This part of the code will be modified session by session

# Train your artificial intelligence by having it solve the maze 1000 times
for episode in range(1000):
    # Choose a random starting point for the game
    x, y = initial_point()

    # This loop will keep the game open so that we can interact with the maze
    while True:
        # Save the previous position
        x_previous = x
        y_previous = y

        # Random action using the next_action function
        action = next_action(x, y, exploration)

        # Calculate the next point
        x, y = next_point(x, y, action)

        # Get the current Q value for that action at the previous position
        current_q_value = q_values[x_previous, y_previous, action]

        # Calculate new Q value
        reward = rewards[x, y]
        temporal_difference = reward + (discount * np.max(q_values[x, y, :])) - current_q_value
        new_q_value = current_q_value + (learning * temporal_difference)

        # Update new Q value
        q_values[x_previous, y_previous, action] = new_q_value
        # Wait and background
        window.fill((0, 0, 0))

        # Draw maze
        draw_maze(x, y)
        pygame.display.flip()

        # End game condition
        if end_game_condition(x, y):
            if rewards[x, y] == 100:
                print("You won!")
            else:
                print("You lost!")
            break

print('Training completed!')

# -------------------------------------------------------------------------
# Draw the shortest path from a position to the goal
def draw_shortest_path(start_x, start_y):
    # Get the shortest path
    path = shortest_path(start_x, start_y)

    # Draw position by position the shortest path
    for i, j in path:
        draw_maze(i, j)
        window.fill((0, 0, 0))
        draw_maze(i, j)
        pygame.display.flip()
        sleep(0.1)


# Test your artificial intelligence to solve the maze from various starting positions
for example in range(3):
    x, y = initial_point()
    draw_shortest_path(x, y)


# -------------------------------------------------------------------------
# Do not delete this line, leave this always until the end
# Close the game
pygame.quit()


