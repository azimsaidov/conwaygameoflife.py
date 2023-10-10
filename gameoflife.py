import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
from matplotlib.patches import Patch



# Constants for cell states
DEAD = 0
ALIVE = 1

grid_size = int(input("Enter the size of the grid: "))

# Create a random grid of cells
grid = np.random.choice([DEAD, ALIVE], size=(grid_size, grid_size))

def update(frameNum, img, grid, grid_size):
    new_grid = grid.copy()
    for i in range(grid_size):
        for j in range(grid_size):
            neighbors_sum = np.sum(grid[i-1:i+2, j-1:j+2]) - grid[i, j]
            if grid[i, j] == ALIVE:
                if neighbors_sum < 2 or neighbors_sum > 3:
                    new_grid[i, j] = DEAD
            else:
                if neighbors_sum == 3:
                    new_grid[i, j] = ALIVE
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img


#Set up the animation
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='gray')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, grid_size),
                              frames=100, interval=200)

labels = ['Dead', 'Alive']

# Define the colors for the legend
colors = ['white', 'black']

# Create a custom legend with the specified labels and colors
legend_elements = [Patch(facecolor=color, edgecolor='black', label=label) for label, color in zip(labels, colors)]
plt.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2)


def start_animation(event):
    ani.event_source.start()

def stop_animation(event):
    ani.event_source.stop()



def on_click(event):
    col = int(event.xdata)
    row = int(event.ydata)
        
        # Toggle the value of the cell
    if grid[row, col] == ALIVE:
        grid[row, col] = DEAD
    else:
        grid[row, col] = ALIVE
        
        # Update the image
    img.set_data(grid)
    fig.canvas.draw_idle()

# Add the click event handler to the image
img.figure.canvas.mpl_connect('button_press_event', on_click)
# Create buttons
start_button = Button(plt.axes([0.95, 0.45, 0.05, 0.1]), 'Start')
start_button.on_clicked(start_animation)

stop_button = Button(plt.axes([0.95, 0.35, 0.05, 0.1]), 'Stop')
stop_button.on_clicked(stop_animation)


plt.show()
