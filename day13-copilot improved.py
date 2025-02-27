from collections import deque


def read_input_file(file_name: str) -> int:
    with open(file_name) as f:
        return int(f.readline().strip())


def make_grid(number: int, size: int) -> list:
    grid = [
        ['.' if bin(x * x + 3 * x + 2 * x * y + y + y * y + number).count('1') % 2 == 0 else '#' for x in range(size)]
        for y in range(size)]
    return grid


def is_valid(grid: list, position: tuple) -> bool:
    return grid[position[1]][position[0]] == '.'


def bfs(file_name: str, start: tuple, goal: tuple = None, max_steps: int = None) -> str:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    number = read_input_file(file_name)
    size = max(goal) + 1 if goal else 60
    grid = make_grid(number, size)
    queue = deque([(0, start)])
    visited = set()

    while queue:
        steps, position = queue.popleft()
        if goal and position == goal:
            return f'goal {goal} reached in {steps} steps'
        if max_steps and steps > max_steps:
            return f'after maximum {max_steps} steps, total reach: {len(visited)}'
        visited.add(position)
        for dx, dy in directions:
            nx, ny = position[0] + dx, position[1] + dy
            if 0 <= nx < size and 0 <= ny < size and is_valid(grid, (nx, ny)) and (nx, ny) not in visited:
                queue.append((steps + 1, (nx, ny)))


if __name__ == '__main__':
    print(f"Part I: {bfs('input/input13.txt', (1, 1), (31, 39))}")
    print(f"Part II: {bfs('input/input13.txt', (1, 1), max_steps=50)}")
