import pygame
import sys
import time

# ---------------- CONFIG ----------------
WIDTH = 600
ROWS = 20
CELL = WIDTH // ROWS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)

pygame.init()
WIN = pygame.display.set_mode((WIDTH, WIDTH))

# -------- NODE CLASS --------
class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.color = WHITE
        self.parent = None

    def draw(self):
        pygame.draw.rect(WIN, self.color,
                         (self.col * CELL, self.row * CELL, CELL, CELL))

    def __lt__(self, other):
        return False

# -------- GRID --------
def make_grid():
    return [[Node(i, j) for j in range(ROWS)] for i in range(ROWS)]


def draw_grid(grid, start, end):
    WIN.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw()

    for i in range(ROWS):
        pygame.draw.line(WIN, BLACK, (0, i*CELL), (WIDTH, i*CELL))
        pygame.draw.line(WIN, BLACK, (i*CELL, 0), (i*CELL, WIDTH))

    start.color = YELLOW
    end.color = RED

    pygame.display.update()

def reset_grid(grid, start, end):
    for row in grid:
        for node in row:
            if node.color not in (BLACK, YELLOW, RED):
                node.color = WHITE
            node.parent = None

def get_neighbors(node, grid):
    r, c = node.row, node.col
    directions = [
        (-1, 0), (0, 1), (1, 0), (1, 1), (0, -1), (-1, -1)
    ]
    neighbors = []
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < ROWS:
            if grid[nr][nc].color != BLACK:
                neighbors.append(grid[nr][nc])
    return neighbors

def reconstruct(end, start, grid):
    current = end
    while current.parent and current != start:
        current = current.parent
        if current != start:
            current.color = PURPLE
        draw_grid(grid, start, end)
        time.sleep(0.05)