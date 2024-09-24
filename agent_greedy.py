import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import math

class VacuumEnvironment:
    def __init__(self, grid_size=(3, 3)):
        self.grid_size = grid_size
        self.rooms = {}
        for i in range(grid_size[0]):
            for j in range(grid_size[1]):
                self.rooms[(i, j)] = random.choice(['clean', 'dirty'])
        self.vacuum_position = (0, 0)  # Vacuum starts in the top-left corner
        self.actions = []

    def clean(self):
        if self.rooms[self.vacuum_position] == 'dirty':
            self.rooms[self.vacuum_position] = 'clean'
            self.actions.append(f"Cleaned {self.vacuum_position}")
        else:
            self.actions.append(f"Room {self.vacuum_position} already clean")

    def move(self):
        # Find all dirty rooms
        dirty_rooms = [pos for pos, state in self.rooms.items() if state == 'dirty']
        
        if not dirty_rooms:
            # If no dirty rooms remain, the vacuum can stop moving
            self.actions.append("No more dirty rooms")
            return
        
        # Get current vacuum position
        x, y = self.vacuum_position

        # Find the nearest dirty room using Manhattan distance
        nearest_dirty_room = min(dirty_rooms, key=lambda room: abs(room[0] - x) + abs(room[1] - y))

        # Move towards the nearest dirty room by one step
        if nearest_dirty_room[0] > x:
            self.vacuum_position = (x + 1, y)  # Move down
        elif nearest_dirty_room[0] < x:
            self.vacuum_position = (x - 1, y)  # Move up
        elif nearest_dirty_room[1] > y:
            self.vacuum_position = (x, y + 1)  # Move right
        elif nearest_dirty_room[1] < y:
            self.vacuum_position = (x, y - 1)  # Move left
        
        self.actions.append(f"Moved to {self.vacuum_position}")

    def all_clean(self):
        return all(state == 'clean' for state in self.rooms.values())

# Visualization function remains the same
def visualize_environment(env, ax):
    ax.clear()
    room_size = 1 / max(env.grid_size)
    for (x, y), state in env.rooms.items():
        color = 'lightgrey' if state == 'clean' else 'red'
        ax.add_patch(patches.Rectangle((y * room_size, (env.grid_size[0] - x - 1) * room_size),
                                       room_size, room_size, edgecolor='black', facecolor=color))
        ax.text((y + 0.5) * room_size, (env.grid_size[0] - x - 0.5) * room_size,
                f"Room {x},{y}\n{state}", fontsize=10, ha='center')

    # Draw vacuum cleaner
    vacuum_x, vacuum_y = env.vacuum_position
    ax.add_patch(patches.Circle(((vacuum_y + 0.5) * room_size, (env.grid_size[0] - vacuum_x - 0.5) * room_size),
                                room_size * 0.3, color='blue'))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.draw()

# Simulation function remains the same
def simulate_vacuum(grid_size=(3, 3)):
    env = VacuumEnvironment(grid_size=grid_size)
    fig, ax = plt.subplots()

    fig.canvas.manager.set_window_title('Vacuum Cleaner World Simulation (Greedy Approach)')

    while not env.all_clean():
        env.clean()
        visualize_environment(env, ax)
        plt.pause(0.5)
        env.move()
        visualize_environment(env, ax)
        plt.pause(0.5)
        
    print("\n".join(env.actions))
    plt.show()

# Run the simulation with a 4x4 grid
simulate_vacuum(grid_size=(4, 4))
