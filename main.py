def locate_element(matrix, target):
    for r, row in enumerate(matrix):
        for c, element in enumerate(row):
            if element == target:
                return r, c
    return None  # If the target is not found

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
target = 5
position = locate_element(matrix, target)

if position:
    print(f"Element {target} found at position {position}")