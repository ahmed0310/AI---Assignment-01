# 📍 Pathfinding Visualizer with Pygame

A high-performance, interactive visualization tool built with **Python** and **Pygame**. This project demonstrates how various pathfinding algorithms navigate a grid, manage frontiers, and handle obstacles to find the most efficient route from a start node to a target.

---

## 🚀 Features

* **Interactive Grid:** Click and drag to place start points, targets, and walls.
* **Real-Time Animation:** Watch the algorithms "think" as they color-code explored vs. frontier nodes.
* **Comprehensive Algorithm Suite:** Compare 6 different search strategies.
* **Visual Path Tracing:** Once a target is found, the optimal path is reconstructed in real-time.

---

## 🛠️ Algorithms Included

| Key | Algorithm | Type | Strategy |
| :--- | :--- | :--- | :--- |
| `1` | **BFS** | Uninformed | Explores layer by layer (Guarantees shortest path). |
| `2` | **DFS** | Uninformed | Explores as deep as possible (Fast, but not optimal). |
| `3` | **UCS** | Uninformed | Account for path cost (Priority Queue based). |
| `4` | **DLS** | Uninformed | DFS with a maximum depth limit. |
| `5` | **IDDFS** | Uninformed | Increases depth limit iteratively (Memory efficient). |
| `6` | **Bidirectional** | Uninformed | Searches from both ends simultaneously. |

---

## 💻 Installation

### Prerequisites
* **Python 3.x**
* **pip** (Python package manager)

### Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/pathfinding-visualizer.git](https://github.com/yourusername/pathfinding-visualizer.git)
   cd pathfinding-visualizer
Install dependencies:

Bash
pip install pygame
Run the application:

Bash
python pathfinding_visualizer.py
🎮 How to Use
Set Start/End: The first two clicks place the Yellow (Start) and Red (End) nodes.

Draw Obstacles: Click and drag to create Black (Wall) nodes that the algorithm must navigate around.

Run Algorithm: Press keys 1 through 6 to start the visualization.

Reset: (Optional: Insert your reset key here, e.g., "Press SPACE to clear").

Visual Legend
🟨 Yellow: Start Node

🟥 Red: Target Node

⬛ Black: Wall / Obstacle

🟩 Green: Frontier (Nodes currently being considered)

🟦 Blue: Explored (Nodes already visited)

🟪 Purple: Final Path

⚙️ Customization
You can easily tweak the simulation parameters within the source code:

Grid Density: Modify the ROWS variable to increase or decrease node count.

Window Size: Adjust the WIDTH constant to fit your display.

Movement Logic: Update the get_neighbors() function to enable or disable diagonal movement.