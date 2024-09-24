# Vacuum Cleaner World Simulation (Greedy Approach)

This repository contains a simulation of a vacuum cleaner navigating a grid of rooms, where each room can be either clean or dirty. The vacuum uses a greedy algorithm to find and clean the nearest dirty room. (Video Demo at end of README)

## Features

- **Grid-Based Environment**: The vacuum operates in a customizable grid size (default is 4x4).
- **Random Room States**: Rooms are randomly initialized as either clean or dirty.
- **Greedy Cleaning Strategy**: The vacuum always moves to the nearest dirty room.
- **Visualization**: The simulation is visualized using Matplotlib, showing the state of each room and the vacuum's position.

## Requirements

To run the simulation, you'll need:

- Python 3.x
- Matplotlib library

You can install the required library using pip:

```bash
pip install matplotlib
```

## How to Run the Simulation

1. Clone this repository:

```bash
git clone https://github.com/David-Okello/Vacuum_Cleaner_World.git
cd Vacuum_Cleaner_World
```

2. Run the simulation script:

```bash
python agent_greedy.py
```

3. The simulation window will open, and you can observe the vacuum cleaning the rooms.
4. Once the simulation is complete a log of actions taken will be displayed in the terminal.

## Code Overview

### ```VacuumEnvironment``` Class

- ```__init__```: Initializes the grid and room states.
- ```clean()```: Cleans the current room if it's dirty.
- ```move()```: Moves the vacuum to the nearest dirty room.
- ```all_clean()```: Checks if all rooms are clean.

### Visualization
The ```visualize_environment()``` function uses Matplotlib to display the current state of the environment.

### Simulation Function
```simulate_vacuum()```: Runs the main simulation loop, updating the environment and visualizing it until all rooms are clean.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Inspired by artificial intelligence and robotics concepts.

## Video Demo
![Screen Recording](./Demo.mp4)