import hashlib
from collections import deque


def read_input_file(file_name: str) -> list:
    """
    Reads the input file and returns the passcode as a string.
    """
    with open(file_name) as f:
        return f.read().strip()


def md5_hash_string(input_string: str) -> str:
    """
    Creates an MD5 hash of the input string and returns the hexadecimal digest.
    """
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()


def is_valid(code: str, direction: str) -> bool:
    """
    Determines if the movement direction is valid based on the MD5 hash of the code.
    Valid directions correspond to characters 'b', 'c', 'd', 'e', and 'f'.
    """
    valid_chars = 'bcdef'
    hashed = md5_hash_string(code)
    direction_indices = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
    return hashed[direction_indices[direction]] in valid_chars


def bfs_shortest_path(passcode: str) -> str:
    """
    Computes the shortest path from the start (0, 0) to the finish (3, 3) using BFS.
    Returns the path as a string.
    """
    directions = {'R': (1, 0), 'D': (0, 1), 'L': (-1, 0), 'U': (0, -1)}
    start = (0, 0)
    finish = (3, 3)
    size = 4
    queue = deque([(0, start, '')])  # (steps, position, path)

    while queue:
        steps, position, path = queue.popleft()
        passcode_path = passcode + path
        if position == finish:
            return path
        for direction, (dx, dy) in directions.items():
            nx, ny = position[0] + dx, position[1] + dy
            if 0 <= nx < size and 0 <= ny < size and is_valid(passcode_path, direction):
                queue.append((steps + 1, (nx, ny), path + direction))
    return "no solution found"


def bfs_longest_path(passcode: str) -> int:
    """
    Computes the longest path from the start (0, 0) to the finish (3, 3) using BFS.
    Returns the number of steps in the longest path.
    """
    directions = {'R': (1, 0), 'D': (0, 1), 'L': (-1, 0), 'U': (0, -1)}
    start = (0, 0)
    finish = (3, 3)
    size = 4
    queue = deque([(0, start, '')])  # (steps, position, path)
    longest_path = 0

    while queue:
        steps, position, path = queue.popleft()
        passcode_path = passcode + path
        if position == finish:
            longest_path = max(longest_path, steps)
        else:
            for direction, (dx, dy) in directions.items():
                nx, ny = position[0] + dx, position[1] + dy
                if 0 <= nx < size and 0 <= ny < size and is_valid(passcode_path, direction):
                    queue.append((steps + 1, (nx, ny), path + direction))
    return longest_path


if __name__ == '__main__':
    input_file = 'input/input17.txt'
    passcode = read_input_file(input_file)
    print(f"Part I: {bfs_shortest_path(passcode)}")
    print(f"Part II: {bfs_longest_path(passcode)} steps")
