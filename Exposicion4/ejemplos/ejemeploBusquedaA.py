import heapq

class Node:
    def __init__(self, x, y, cost, parent=None):
        self.x = x
        self.y = y
        self.cost = cost
        self.parent = parent
    
    def __lt__(self, other):
        return self.cost < other.cost
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def astar_search(start, goal, h_func, get_neighbors_func):
    frontier = []
    heapq.heappush(frontier, start)
    came_from = {start: None}
    cost_so_far = {start: 0}
    
    while frontier:
        current = heapq.heappop(frontier)
        
        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for neighbor in get_neighbors_func(current):
            new_cost = cost_so_far[current] + neighbor.cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + h_func(goal, neighbor)
                neighbor.cost = new_cost
                heapq.heappush(frontier, neighbor)
                came_from[neighbor] = current
    
    return None

def manhattan_distance(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)

def get_neighbors(node, grid):
    neighbors = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x = node.x + dx
        y = node.y + dy
        if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[x]) and not grid[x][y]:
            neighbors.append(Node(x, y, 0))
    return neighbors

def print_map(map, path=None):
    for x in range(len(map)):
        for y in range(len(map[x])):
            if (x, y) == start:
                print("S", end="")
            elif (x, y) == goal:
                print("G", end="")
            elif path and (x, y) in path:
                print("*", end="")
            elif map[x][y]:
                print("#", end="")
            else:
                print(".", end="")
        print()

# Ejemplo de uso
map = [[False, False, False, False, False],
       [False, True, False, True, False],
       [False, True, False, True, False],
       [False, True, False, True, False],
       [False, False, False, False, False]]

start = Node(0, 0, 0)
goal = Node(4, 4, 0)

path = astar_search(start, goal, manhattan_distance, lambda n: get_neighbors(n, map))
print_map(map, path)