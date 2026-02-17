import pygame
import sys
import time
from collections import deque
import heapq

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


# -------- BFS ALGORITHM --------
def bfs(start, end, grid):
    q = deque([start])
    visited = set([start])

    while q:
        pygame.event.pump()
        node = q.popleft()

        if node == end:
            reconstruct(end, start, grid)
            return

        for neighbor in get_neighbors(node, grid):
            if neighbor not in visited:
                visited.add(neighbor)
                neighbor.parent = node
                if neighbor != end:
                    neighbor.color = GREEN
                q.append(neighbor)

        if node != start and node != end:
            node.color = BLUE

        draw_grid(grid, start, end)
        time.sleep(0.02)


# -------- DFS ALGORITHM --------
def dfs(start, end, grid):
    stack = [start]
    visited = set()

    while stack:
        pygame.event.pump()
        node = stack.pop()

        if node == end:
            reconstruct(end, start, grid)
            return

        if node not in visited:
            visited.add(node)
            if node != start and node != end:
                node.color = BLUE

            for neighbor in reversed(get_neighbors(node, grid)):
                if neighbor not in visited:
                    neighbor.parent = node
                    if neighbor != end:
                        neighbor.color = GREEN
                    stack.append(neighbor)

        draw_grid(grid, start, end)
        time.sleep(0.02)


# -------- UCS ALGORITHM --------
def ucs(start, end, grid):
    pq = []
    heapq.heappush(pq, (0, start))
    visited = set()

    while pq:
        pygame.event.pump()
        cost, node = heapq.heappop(pq)

        if node == end:
            reconstruct(end, start, grid)
            return

        if node not in visited:
            visited.add(node)
            if node != start and node != end:
                node.color = BLUE

            for neighbor in get_neighbors(node, grid):
                if neighbor not in visited:
                    neighbor.parent = node
                    heapq.heappush(pq, (cost+1, neighbor))
                    if neighbor != end:
                        neighbor.color = GREEN

        draw_grid(grid, start, end)
        time.sleep(0.02)

# ------------MAIN LOOP ------------
def main():
    grid = make_grid()
    start = grid[2][2]
    end = grid[17][17]

    start.color = YELLOW
    end.color = RED

    for i in range(5, 15):
        grid[i][10].color = BLACK

    draw_grid(grid, start, end)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                reset_grid(grid, start, end)

                if event.key == pygame.K_1:
                    bfs(start, end, grid)
                if event.key == pygame.K_2:
                    dfs(start, end, grid)
                if event.key == pygame.K_3:
                    ucs(start, end, grid)
                # if event.key == pygame.K_4:
                #     dls(start, end, grid, limit=20)
                # if event.key == pygame.K_5:
                #     iddfs(start, end, grid)
                # if event.key == pygame.K_6:
                #     bidirectional(start, end, grid)

        draw_grid(grid, start, end)

main()
