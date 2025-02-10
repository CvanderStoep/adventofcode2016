import re

def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        return [list(map(int, re.findall(r'\d+', line))) for line in f]

def check_valid_triangle(a: int, b: int, c: int) -> bool:
    # Check if the given sides form a valid triangle
    return a + b > c and a + c > b and b + c > a

def compute_part_two(file_name: str) -> str:
    triplets = read_input_file(file_name)
    valid_triplets = 0

    # Process triplets column-wise
    for i in range(0, len(triplets), 3):
        for j in range(3):
            a, b, c = triplets[i][j], triplets[i+1][j], triplets[i+2][j]
            if check_valid_triangle(a, b, c):
                valid_triplets += 1

    return f'valid_triplets = {valid_triplets}'

# Example usage
file_name = 'example.txt'  # Replace with your actual file name
result = compute_part_two(file_name)
print(result)
