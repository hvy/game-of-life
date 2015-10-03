"""

A simple Game of Life implementation using numpy and matplotlib for
visualization.

Reference:
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

"""

# Change the backend to TKAgg to allow animations from  non-gui Python shells
import matplotlib
matplotlib.use('TKAgg')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def iter(i):
  """Simulates a step.

  :param i: the iteration/frame number
  """
  # Get the 2-dimensional world array
  world = im.get_array()

  # Count the number of neighbors for all positions
  neighbors = (world[0:-2, 0:-2] + world[0:-2, 1:-1] + world[0:-2, 2:] +
               world[1:-1, 0:-2] + world[1:-1, 2:] + world[2:, 0:-2] +
               world[2:, 1:-1] + world[2:, 2:])

  # Update the world according to the rules (see reference link)
  birth = (neighbors == 3) & (world[1:-1, 1:-1] == 0)
  survive = ((neighbors == 2) | (neighbors == 3)) & (world[1:-1, 1:-1] == 1)
  world[...] = 0
  world[1:-1, 1:-1][birth | survive] = 1

  # Update
  im.set_array(world)

  return [im]

def init():
  """Initialize the animation window.
  """
  im.set_data(world)

  return [im]

def generate(width, height):
  """Generates a random population with the given window width and height.

  :param width: the width of the window
  :param height: the height of the window
  """
  # Return a binary 2-dimensional array
  return np.random.randint(2, size=(width, height))

# Create the initial world
width = 100
height = 100
world = generate(width, height)

# Create the figure and put one graph inside it representing the world
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlim([0, width])
ax.set_ylim([0, height])

# Plot the 2-dimensional world in the figure
im = plt.imshow(world, interpolation='nearest', cmap=plt.cm.gray_r)

# Configure the animation and set blit to True to only redraw the updated
# pixels. The animation needs to persist, hence the assignment
anim = animation.FuncAnimation(fig, iter, frames=360, interval=100, blit=True)

# Show the figure and start the animation
plt.show()

