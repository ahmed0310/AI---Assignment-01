# Pathfinding Visualizer with Pygame

A visual demonstration of common pathfinding algorithms using **Python** and **Pygame**. Watch how different algorithms explore a grid to find the shortest path from a start node to a target node.

---

## Features

- Grid-based visualization
- Interactive start and target nodes
- Obstacle/wall support
- Real-time animation of algorithm exploration
- Supports multiple algorithms:
  - **Breadth-First Search (BFS)**
  - **Depth-First Search (DFS)**
  - **Uniform-Cost Search (UCS)**
  - **Depth-Limited Search (DLS)**
  - **Iterative Deepening DFS (IDDFS)**
  - **Bidirectional Search**

---

## Installation

1. Make sure you have **Python 3.x** installed.
2. Install `pygame`:

```bash
pip install pygame
Download or clone this repository.

Run the program:

python pathfinding_visualizer.py
Usage
The grid is 20x20 cells by default.

Start node: Yellow

End node: Red

Wall/obstacle: Black

Frontier nodes (nodes being explored): Green

Explored nodes: Blue

Final path: Purple

Keyboard Controls (select algorithm):

Key	Algorithm
1	Breadth-First Search (BFS)
2	Depth-First Search (DFS)
3	Uniform-Cost Search (UCS)
4	Depth-Limited Search (DLS)
5	Iterative Deepening DFS (IDDFS)
6	Bidirectional Search
Quit: Close the window or press ESC.

How It Works
The program initializes a grid of nodes.

Users can set walls and watch how algorithms explore paths from start → end.

Each algorithm uses its own exploration strategy:

BFS/DFS: Queue/Stack

UCS: Priority queue (cost-based)

DLS/IDDFS: Depth-limited iterations

Bidirectional: Two BFS searches meet in the middle

The final path is traced back from the target node to the start node.

Customization
Change grid size by modifying ROWS.

Adjust window width by changing WIDTH.

Change colors for nodes by updating the color variables.

Add or remove diagonal movement in the get_neighbors() function.

Dependencies
Python 3.x

Pygame (pip install pygame)